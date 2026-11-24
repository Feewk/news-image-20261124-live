// THE WORLD TODAY — Tuesday, 24 November 2026 (Node 22, stdlib only).
// Copies the committed entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
// (default /output/entry.png). Deterministic: a plain byte copy.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
