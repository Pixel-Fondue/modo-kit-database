-- Create the authors table
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, -- The name of the author/company.
    -- The following fields are optional.
    has_avatar BOOLEAN, -- Whether the author has an avatar to display.
    handle TEXT,        -- The author's handle.
    links TEXT          -- A JSON object containing links to the author's social media.
);
