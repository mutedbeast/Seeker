# Seeker 🔦🛡️

**A lightweight reconnaissance tool for red team operations**

Seeker is a focused reconnaissance utility designed for offensive security practitioners and red teamers. It combines directory enumeration and port scanning capabilities in a single, scriptable tool optimized for operational security and workflow integration.

```
  _________              __
 /   _____/ ____   ____ |  | __ ___________
 \_____  \_/ __ \_/ __ \|  |/ // __ \_  __ \
 /        \  ___/\  ___/|    <\  ___/|  | \/
/_______  /\___  >\___  >__|_ \\___  >__|
        \/     \/     \/     \/    \/
```

## ⚠️ Legal Disclaimer

**USE RESPONSIBLY AND LEGALLY**

Seeker is intended for authorized security testing only. Users must:
- Have explicit written permission to test target systems
- Comply with all applicable laws and regulations
- Follow responsible disclosure practices

Unauthorized scanning is **illegal and unethical**. The authors assume no liability for misuse.

## 🎯 Core Capabilities

### Directory Scanning
Enumerate web application paths and endpoints to discover:
- Hidden admin panels and management interfaces
- Backup files and forgotten endpoints
- API endpoints and documentation
- Configuration files and sensitive resources

### Port Scanning
Lightweight reconnaissance of target hosts to identify:
- Open services and their ports
- Potential attack surface
- Service fingerprinting opportunities

## 🚀 Features

- **Dual Operation Modes**: Interactive prompts or CLI arguments for automation
- **Custom Wordlists**: Pluggable wordlist support for targeted enumeration
- **Operational Flexibility**: Configurable timeouts and verbosity levels
- **Scriptable Interface**: Easy integration with red team playbooks and C2 frameworks
- **Minimal Footprint**: Lean design for containerized toolchains
- **Cross-Platform**: Works on Windows, Linux, and macOS

## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- Network access to target systems

### Dependencies
- `requests` - HTTP/HTTPS request handling
- `argparse` - Command-line argument parsing (standard library)

Install dependencies:
```bash
pip install -r requirements.txt
```

**Recommended**: Use a virtual environment to isolate dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/mutedbeast/seeker.git
cd seeker
```

2. Set up virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Verify installation:
```bash
python seeker.py --help
```

## 💻 Usage

### Interactive Mode

For quick, ad-hoc reconnaissance operations:

```bash
python seeker.py
```

**Example Session:**
```bash
$ python seeker.py
  _________              __
 /   _____/ ____   ____ |  | __ ___________
 \_____  \_/ __ \_/ __ \|  |/ // __ \_  __ \
 /        \  ___/\  ___/|    <\  ___/|  | \/
/_______  /\___  >\___  >__|_ \\___  >__|
        \/     \/     \/     \/    \/

Enter the target : https://example.com

Choose one operation
 1. Directory Scanning
 2. Port Scanning
Enter your operation : 1

Choose a wordlist file
 Type C for common wordlist
 A for all
 Path of custom wordlist: /path/to/custom/wordlist.txt

https://example.com/admin
https://example.com/help
https://example.com/api
```

### CLI Mode (Automation)

For scripted operations and integration with red team workflows:

**Directory Scanning:**
```bash
python seeker.py -t https://target.com -o d -c /path/to/wordlist.txt
```

**Using Built-in Wordlists:**
```bash
# Common wordlist
python seeker.py -t https://target.com -o d -c C

# All wordlists
python seeker.py -t https://target.com -o d -c A
```

**Port Scanning:**
```bash
python seeker.py -t 192.168.1.100 -o p
```

### Command-Line Arguments

```bash
python seeker.py [OPTIONS]

Options:
  -t, --target    Target URL or IP address (required in CLI mode)
  -o, --operation Operation type: 'd' for directory scan, 'p' for port scan
  -c, --command   Wordlist selection: 'C' (common), 'A' (all), or custom path
  -h, --help      Show help message and exit
```

## 📚 How It Works

### Directory Scanning Workflow

1. **Target Input**: Accepts URL in format `https://target.com`
2. **Wordlist Selection**: Loads predefined or custom wordlists
3. **Path Enumeration**: Iterates through wordlist, appending paths to base URL
4. **HTTP Requests**: Sends GET requests to each constructed URL
5. **Response Analysis**: Identifies accessible endpoints based on status codes
6. **Result Output**: Displays discovered URLs in real-time

### Port Scanning Workflow

1. **Target Input**: Accepts IP address or hostname
2. **Port Range**: Scans common ports or custom range
3. **Socket Connection**: Attempts TCP connection to each port
4. **Service Detection**: Identifies open ports and running services
5. **Result Output**: Lists accessible ports and detected services

### Operational Security Considerations

- Configurable request delays to avoid detection
- User-agent customization options
- Timeout controls for stealth operations
- Result logging for documentation and reporting

## 🔬 Red Team Use Cases

### Reconnaissance Phase
- Initial surface mapping of web applications
- Service discovery during external assessments
- Identifying forgotten or undocumented endpoints

### Integration with Toolchains
```bash
# Pipe results to further analysis
python seeker.py -t https://target.com -o d -c C > discovered_paths.txt

# Combine with other tools
python seeker.py -t target.com -o p | grep "OPEN" | awk '{print $1}' | xargs -I {} nmap -sV -p {} target.com
```

### Automated Playbooks
```python
# Example integration in Python automation
import subprocess

targets = ["https://target1.com", "https://target2.com"]
for target in targets:
    subprocess.run(["python", "seeker.py", "-t", target, "-o", "d", "-c", "C"])
```

## 📂 Project Structure

```
seeker/
├── seeker.py              # Main script
├── directory_scanner.py   # Directory enumeration module
├── port_scanner.py        # Port scanning module
├── wordlists/            # Built-in wordlist directory
│   ├── common.txt
│   └── all.txt
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── LICENSE               # MIT License
└── contributing.md       # Contribution guidelines
```

## 🛠️ Libraries Used

- **requests** (`v2.31.0+`): HTTP library for directory enumeration with robust session handling and SSL support
- **argparse** (standard library): Command-line argument parsing for CLI mode
- **socket** (standard library): Low-level networking for port scanning operations
- **concurrent.futures** (standard library): Thread pooling for concurrent operations (if implemented)

## 🤝 Contributing

Contributions are welcome! This project benefits from community input.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/enhancement`)
5. Open a Pull Request

See `contributing.md` for detailed guidelines and code of conduct.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**MIT License Summary**: Free to use, modify, and distribute with attribution.

## 👤 Author

**@mutedbeast**
- GitHub: [@mutedbeast](https://github.com/mutedbeast)

## 🙏 Acknowledgments

- Inspired by industry-standard tools like DirBuster, Gobuster, and Nmap
- Built for the offensive security community
- Thanks to all contributors and security researchers

## 📞 Support & Contact

- **Issues**: Report bugs via [GitHub Issues](https://github.com/mutedbeast/seeker/issues)
- **Security**: Report vulnerabilities privately to maintain responsible disclosure

## 🔄 Version History

- **v1.0.0** - Initial release with directory and port scanning capabilities

---

**Remember**: Always scan responsibly. Ethical hacking makes the internet safer. 🛡️