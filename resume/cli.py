import os
import argparse
import re
from .builder import build


def main():
    parser = argparse.ArgumentParser(description='Build resumes')
    parser.add_argument('cmd', default='build', help='one of {build}')
    parser.add_argument('-t', '--template_dir', default='templates',
                        help='path to templates directory')
    parser.add_argument('-o', '--output_dir', help='path to output directory',
                        default='output')
    parser.add_argument('-c', '--content', help='path to cv.xml',
                        default='content/cv.xml')
    parser.add_argument('filter', nargs='*', default='txt',
                        help='only build templates matching this regex')
    args = parser.parse_args()
    if args.cmd == 'build':
        regex = re.compile('|'.join(args.filter))
        for template in os.listdir(args.template_dir):
            if regex.search(template) is not None:
                build(
                    os.path.abspath(
                        os.path.join(
                            args.output_dir, re.sub('\.jinja$', '', template)
                        )
                    ),
                    os.path.abspath(
                        os.path.join(args.template_dir, template)
                    ),
                    os.path.abspath(args.content)
                )
    else:
        print('%s: not yet implemented'.format(args.cmd))


if __name__ == '__main__':
    main()
