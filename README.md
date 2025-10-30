# Blinky Lights

An Electron-powered homage to the hypnotic blinking indicators of classic data centers. The app renders stylized server racks with ever-shifting status LEDs, load meters, and activity sweeps to recreate the ambient glow operators used to watch from the NOC.

## Prerequisites
- Node.js 18+ and npm.
- macOS build tools (Xcode Command Line Tools) for packaging a `.app` or `.dmg`.

## Getting Started
```bash
npm install
npm start
```
`npm start` launches the Electron development environment with hot reload of renderer assets.

## Packaging for macOS
```bash
npm run build
```
The command invokes `electron-builder` to produce both `.dmg` and `.zip` artifacts under `dist/`. Use `npm run pack` for unpackaged output inside `dist/mac`.

## Project Structure
- `src/main.js` – Electron main process, window setup, and lifecycle handling.
- `src/preload.js` – Secure bridge exposing limited metadata to the renderer.
- `src/renderer/` – HTML, CSS, and JavaScript powering the animated rack wall.

## Customizing the Experience
- Tweak rack and light counts in `src/renderer/renderer.js`.
- Adjust color palettes and animation curves in `src/renderer/styles.css`.
- Replace the copy in `src/renderer/index.html` to tailor the nostalgia hit for your team.

## Notes
- Code is written for dark mode and expects the window to be at least 960×600.
- `electron` and `electron-builder` are listed as devDependencies; install them before running the app.
# blinky_lights
