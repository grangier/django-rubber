"""
Management command for rubber.
"""
import os
import sys

from rubber.management.base import ESBaseCommand


class Command(ESBaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('indexes',
            action='store',
            type=str,
            nargs='*',
            help=(
                "List of indexes names to create"
            )
        )
        parser.add_argument('--dry-run',
            action='store_true',
            dest='dry_run',
            default=False,
            help=(
                "Run the command in dry run mode without actually changing "
                "anything."
            )
        )

    def run(self, *args, **options):
        if len(options['indexes']) == 0:
            self.print_error("Please provide at least one index.")
            sys.exit(1)
        for index in options['indexes']:
            config_path = os.path.join(
                self.rubber_config.config_root,
                '{0}.json'.format(index)
            )
            self.print_info(u"Using config file : {0}".format(config_path))
            body = None
            try:
                with open(config_path, 'r') as f:
                    body = f.read()
            except IOError:
                self.print_error("Config file does not exist.")
                continue
            self.rubber_config.es.indices.create(index=index, body=body)
            self.print_success(u"Index {0} created.".format(index))
