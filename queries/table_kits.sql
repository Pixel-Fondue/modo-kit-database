-- Create the kits table
CREATE TABLE IF NOT EXISTS kits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,         -- The name attribute from index.cfg.
    label TEXT NOT NULL,        -- The nice name of the kit to display.
    author TEXT NOT NULL,       -- The original author of the kit.
    version TEXT NOT NULL,      -- The current version of the kit.
    description TEXT NOT NULL,  -- The description of the kit for users.
    search TEXT NOT NULL,       -- The search string for the kit.
    -- The following fields are optional.
    url TEXT,                   -- The URL to the kit's homepage.
    help TEXT,                  -- The URL to the kit's help page.
    manifest TEXT,              -- The manifest.json file for the kit installation.
    has_banner BOOLEAN,         -- Whether the kit has a banner.
    installable BOOLEAN         -- Whether the kit is installable via MKC.
);
