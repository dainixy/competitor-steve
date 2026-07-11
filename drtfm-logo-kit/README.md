# DRT.FM Logo Kit — The Heartwave

Locked 2026-07-11. Mark: seven rose sound bars tracing a heart (love + .fm). Lockup: mark + `drt.fm` in Satoshi Bold outlines (no font dependency — all text is vector paths).

## Files

| File | Use |
|---|---|
| `lockup-dark.svg` | **Primary logo** — headers, footers, anything on dark |
| `lockup-dark-animated.svg` | Same, bars pulse — only while Alexis speaks / as loader |
| `lockup-light.svg` | On white/light (email, invoices, ads) |
| `lockup-mono-white.svg` / `lockup-mono-black.svg` | Single-color contexts (engraving, watermark, partner docs) |
| `wordmark-only-dark/light.svg` | Text without the mark (tight spaces where the favicon is already visible) |
| `mark.svg` / `mark-animated.svg` / `mark-mono-*.svg` | The Heartwave alone |
| `favicon.ico`, `favicon-16/32/48/64.png` | Browser tab (transparent background) |
| `app-icon-180.png` | iOS `apple-touch-icon` |
| `app-icon-192.png`, `app-icon-512.png` | PWA manifest icons |
| `favicon-512-master.png` | Transparent master for any future raster need |

## Drop into `<head>`

```html
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/mark.svg">
<link rel="apple-touch-icon" href="/app-icon-180.png">
```

## Rules (mirror of DRTFM-DESIGN.md §12)

- One heart per surface: if the lockup is visible, no other hearts nearby.
- Animated variant: only while she speaks or as a loading state; never autoplaying on marketing pages; both animated files respect `prefers-reduced-motion`.
- Below 20px lockup height, use `mark.svg` alone.
- Clear space = one bar-width around the lockup. Never recolor outside rose `#f2436b` / white `#f2f0f3` / ink `#17161a`.
