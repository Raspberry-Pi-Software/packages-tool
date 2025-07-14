# packages-tool
A simple packages tool for loading and unloading packages to your Raspberry Pi (supported model)

## Use the packages tool
Use this command to install the packages tool onto your Pi:
```bash
git clone https://github.com/Raspberry-Pi-Software/packages-tool && cd packages-tool && sudo bash install;
```
Use this command to remove the packages tool from your Pi:
```bash
cd packages-tool && sudo bash uninstall;
```

## Usage
The packages tool provides APT-like functionality for managing Raspberry Pi Software packages:
```bash
rpisft [command] [package]
```

### Available Commands:
- `install <package>` - Install a package from the Raspberry Pi Software repository
- `add <package>` - Alias for install
- `uninstall <package>` - Uninstall an installed package
- `remove <package>` - Alias for uninstall  
- `delete <package>` - Alias for uninstall
- `update` - Update the package list from GitHub
- `upgrade` - Upgrade all installed packages
- `force-upgrade` - Force upgrade all packages (skips pre-uninstall scripts)
- `list` - List all installed packages
- `search <term>` - Search for available packages matching the term

### Examples:
```bash
# Install a package
rpisft install device-manager

# Update package list
rpisft update

# List installed packages
rpisft list

# Search for packages
rpisft search gpio

# Upgrade all packages
rpisft upgrade

# Uninstall a package
rpisft uninstall device-manager
```

### Available Packages:
The tool automatically fetches packages from the [Raspberry-Pi-Software organization](https://github.com/Raspberry-Pi-Software) on GitHub. Use `rpisft update` to see the current list of available packages.
