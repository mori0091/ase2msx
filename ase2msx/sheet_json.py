# -*- coding: utf-8-unix -*-

# Copyright (c) 2025 Daishi Mori (mori0091)
#
# This software is released under the MIT License.
# See https://github.com/mori0091/ase2msx

def load(path):
    import json
    import re

    with open(path) as f:
        d = json.load(f)

        # assert(d['meta']['app'] == "https://www.aseprite.org/")

        # format = d['meta']['format']
        # print(f'format: {format}')

        # size = d['meta']['size']
        # print(f'size: {size}')

        # layers = d['meta']['layers']
        # for i, layer in enumerate(layers):
        #     # for debug
        #     print(f'# layer #{i}: {layer}')

        # frameTags = d['meta']['frameTags']
        # for i, tag in enumerate(frameTags):
        #     print(f'frameTag #{i}: {tag}')

        frames = d['frames']
        framelist = []
        celset = set()
        for cel_filename, frame in frames.items():
            m = re.match(r'[^\s]+(\s+\((.*)\))?(\s+([0-9]+))?.*', cel_filename)
            layer, frame_number = m.group(2,4)
            if frame_number == None:
                frame_number = 0
            else:
                frame_number = int(frame_number)
            # m = re.match(r'[^\s]+\s*.*\s*([0-9]+).*', cel_filename)
            # frame_number = int(m.group(1))
            xywh = frame['frame']
            duration = frame['duration']
            # for debug
            # print(f"# frame #{frame_number} ({layer}): {duration}ms {xywh}")
            cel = repr(xywh)
            celset.add(cel)
            if len(framelist) <= frame_number:
                framelist.append({'duration': duration, 'cels': [xywh]})
            else:
                framelist[frame_number]['cels'].append(xywh)

        frames = framelist
        cels = [eval(cel) for cel in sorted(celset)]
        for frame in frames:
            frame['cels'] = [cels.index(xywh) for xywh in reversed(frame['cels'])]

        return {
            'format'   : d['meta']['format'],
            'size'     : d['meta']['size'],
            'frameTags': d['meta'].get('frameTags', []),
            'frames'   : frames,
            'cels'     : cels,
        }

def dump(d):
    # import json
    # print(json.dumps(d, indent=2))
    for key, value in d.items():
        if isinstance(value, list):
            for i, a in enumerate(value):
                print(f'# {key} #{i}: {repr(a)}')
        else:
            print(f'# {key}: {repr(value)}')
