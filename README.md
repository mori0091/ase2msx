# ase2msx ; Creates sprite data for libmsx/MSX2 from aseprite file.

## LICENSE

Copyright (c) 2025 Daishi Mori (mori0091)

This software is released under the MIT License.  

GitHub libmsx project  
<https://github.com/mori0091/libmsx>

## Requirements

- ***Python** (https://www.python.org/)
- **aseprite** (https://www.aseprite.org/) ; Animated Sprite Editor & Pixel Art Tool

## Install

``` shell
pip install ase2msx-X.Y.tar.gz
```
where `X.Y` is released version number.

## Usage

``` shell
ase2msx A.ase
```

Creates sprite data for libmsx/MSX2 from aseprite file `A.ase`.  

The following files will be generated:
- aseprite's meta-data     : `A.json` (exported by aseprite)
- aseprite's sprite sheet  : `A.png` (exported by aseprite)
- C header file for libmsx : `A.h`
- C source file for libmsx : `A.c`
- spritte data for libmsx  : `A.sm2`

The sprite must be
- Multiple of 16x16 pixels
- IndexColor w/ up to 16 colors
- color code #0 is transparent

See also `libmsx` project on GitHub for more detail.  
- [GitHub libmsx project](https://github.com/mori0091/libmsx)
- [TUTORIAL : SM2 (Sprite Mode 2) - Animated Color Sprites](https://github.com/mori0091/libmsx/tree/main/docs/tutorial_SM2.md)
