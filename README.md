# Core modo kit database for external tools to connect to.

# How to add your kits:
1. Make a formal request on the Pixel Fondue Discord in the #modo-kit-central channel.
2. Make a PR request to this repo with your kit info.
   1. Fork this repo.
   2. Add your `info.json` file to the `kits` folder.
   3. Make a PR request to this repo.
   4. Once approved, your kit will be added to the database automatically.


## `info.json` example
```JSON5
{
  // The nice-name of the kit.
  // This is what will be displayed in the UI.
  "label": "Modo Kit Central",
  // The index.cfg kit name: 
  // <configuration kit="MODO_KIT_CENTRAL" version="1.30" and="rel]1500">
  // This is what's used to identify if the kit is installed.
  "name": "MODO_KIT_CENTRAL",
  // The author of the kit.
  "author": "Pixel Fondue",
  // The source of the kit. Gumroad, GitHub, etc.
  "source": "GitHub",
  // The desctiption that will be displayed in the UI.
  "description": "Kit to help you find and install kits for Modo.",
  // If the kit can be installed from MKC (Requires an accessible manifest and lpk file).
  "installable": true,
  // Path to the manifest.json file to check for updates and install the kit (if installable).
  "manifest": "https://github.com/Pixel-Fondue/modo-kit-central/releases/latest/download/modo_kit_central_0.1.9.lpk",
  // The URL of the source of the kit to send users to.
  // This is used to open the source in the browser.
  "url": "https://github.com/Pixel-Fondue/modo-kit-central",
  // A url to redirect users to for help., community forums, discord, etc.
  "help": "https://github.com/Pixel-Fondue/modo-kit-central",
  // Terms that, when searched in the UI, will return this kit.
  "search": ["modo", "kits", "install", "python", "search"]
}
```
