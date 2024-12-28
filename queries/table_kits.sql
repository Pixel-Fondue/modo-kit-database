-- Create the kits table
CREATE TABLE IF NOT EXISTS kits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,         -- The name attribute from index.cfg.
    label TEXT NOT NULL,        -- The nice name of the kit to display.
    author TEXT NOT NULL,       -- The original author of the kit.
    version TEXT NOT NULL,      -- The current version of the kit.
    description TEXT NOT NULL,  -- The description of the kit for users.
    url TEXT,                   -- The URL to the kit's homepage.
    help TEXT,                  -- The URL to the kit's help page.
    installable BOOLEAN,        -- Whether the kit is installable via MKC.
    manifest TEXT,              -- The manifest.json file for the kit installation.
    search TEXT NOT NULL        -- The search string for the kit.
);
