import math

# 5x7 Bitmap font for BLACK0X80
font = {
    'B': ['11110', '10001', '11110', '10001', '11110'],
    'L': ['10000', '10000', '10000', '10000', '11111'],
    'A': ['01110', '10001', '11111', '10001', '10001'],
    'C': ['01111', '10000', '10000', '10000', '01111'],
    'K': ['10001', '10010', '11100', '10010', '10001'],
    '0': ['01110', '10001', '10001', '10001', '01110'],
    'X': ['10001', '01010', '00100', '01010', '10001'],
    '8': ['01110', '10001', '01110', '10001', '01110']
}

word = 'BLACK0X80'
grid_w = 60
grid_h = 10
cell_size = 10
gap = 2

text_width = len(word) * 6 - 1
start_x = (grid_w - text_width) // 2
start_y = 2

active_cells = set()

for i, char in enumerate(word):
    bitmap = font[char]
    for r, row in enumerate(bitmap):
        for c, bit in enumerate(row):
            if bit == '1':
                gx = start_x + (i * 6) + c
                gy = start_y + r
                active_cells.add((gx, gy))

svg = f'''<svg width="800" height="180" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .bg {{ fill: #050505; stroke: #00ff00; stroke-width: 2; }}
      .dot {{ fill: #001a00; rx: 2; ry: 2; }}
      .dot-active {{ fill: #00cc00; rx: 2; ry: 2; filter: drop-shadow(0 0 4px #00ff00); }}
      
      .snake {{
        fill: none;
        stroke: #00ff00;
        stroke-width: {cell_size};
        stroke-linecap: square;
        stroke-linejoin: miter;
        filter: drop-shadow(0 0 6px #00ff00);
        stroke-dasharray: 200 4000;
        animation: crawl 8s linear infinite;
      }}
      
      @keyframes crawl {{
        0% {{ stroke-dashoffset: 4000; }}
        100% {{ stroke-dashoffset: 0; }}
      }}
      
      .text-glow {{ fill: #00ff00; font-family: 'Courier New', monospace; font-weight: bold; font-size: 14px; text-shadow: 0 0 5px #00ff00; }}
      .scanline {{ fill: rgba(0, 255, 0, 0.1); animation: scan 3s linear infinite; }}
      @keyframes scan {{ 0% {{ transform: translateY(-100%); }} 100% {{ transform: translateY(200%); }} }}
    </style>
  </defs>

  <rect width="100%" height="100%" rx="4" class="bg" />
  <rect width="100%" height="40" class="scanline" />
  
  <g transform="translate(38, 30)">
'''

# Draw all grid dots
for y in range(grid_h):
    for x in range(grid_w):
        px = x * (cell_size + gap)
        py = y * (cell_size + gap)
        if (x, y) in active_cells:
            svg += f'    <rect x="{px}" y="{py}" width="{cell_size}" height="{cell_size}" class="dot-active" />\\n'
        else:
            svg += f'    <rect x="{px}" y="{py}" width="{cell_size}" height="{cell_size}" class="dot" />\\n'

# Generate a continuous snake path weaving across the active text.
# The snake will enter from top left, sweep back and forth over the letters, and exit top right.
path_d = f"M -50 {start_y * (cell_size + gap)} "
for x in range(start_x, start_x + text_width + 1):
    px = x * (cell_size + gap)
    # alternate up and down
    if (x - start_x) % 2 == 0:
        path_d += f"L {px} {start_y * (cell_size + gap)} "
        path_d += f"L {px} {(start_y + 4) * (cell_size + gap)} "
    else:
        path_d += f"L {px} {(start_y + 4) * (cell_size + gap)} "
        path_d += f"L {px} {start_y * (cell_size + gap)} "

path_d += f"L {grid_w * (cell_size + gap) + 50} {start_y * (cell_size + gap)}"

svg += f'''
    <!-- The Matrix Snake -->
    <path d="{path_d}" class="snake" />
  </g>
  
  <!-- Cyberpunk UI Elements -->
  <path d="M 0 30 L 20 30 L 40 10 L 760 10 L 780 30 L 800 30" fill="none" stroke="#00ff00" stroke-width="2" opacity="0.7"/>
  <text x="400" y="22" text-anchor="middle" class="text-glow">[ OVERRIDE // BLACK0X80 :: MATRIX_GRID_ACTIVE ]</text>
  <text x="400" y="170" text-anchor="middle" class="text-glow">TARGET SEQUENCE: B L A C K 0 X 8 0</text>
  
  <!-- Corner nodes -->
  <rect x="10" y="40" width="4" height="100" fill="#00ff00" opacity="0.5" />
  <rect x="786" y="40" width="4" height="100" fill="#00ff00" opacity="0.5" />
</svg>
'''

with open('images/cyber_snake.svg', 'w') as f:
    f.write(svg)
print('Generated cyber_snake.svg')
