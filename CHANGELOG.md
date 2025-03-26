## Changelog

- Creating new embedded modules changed for using existing ones (needed for proper launch under venv; reverse compatible change)
- Entry point module now will be added to ``sys.path`` on the server launch
- Server will now throw an exception if entry point module doesn't exist
- Fix for ``Packet.sendToAll`` had incorrect argument list