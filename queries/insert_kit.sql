-- Desc: Insert a new kit into the database
INSERT INTO kits (
    name, label, author, version, description, search, url, help, manifest, has_banner, installable
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
