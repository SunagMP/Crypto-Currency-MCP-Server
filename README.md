# 🪙 CoinGecko MCP Server

This repository provides a custom **CoinGecko MCP Server** built using [FastMCP](https://github.com/fastmcp/fastmcp). It allows integration with **Claude Desktop** to fetch live cryptocurrency prices and related data directly through an MCP connection.

---

## 🚀 Setup Instructions

Follow the steps below to run and integrate your MCP server with **Claude Desktop**.

---
### **Step 1: Test MCP Server Using MCP Inspector**
Before installing, test whether your MCP server is working properly using the **MCP Inspector**.
```bash
uv run fastmcp dev main.py
```
If the server starts successfully, you should see log outputs indicating the MCP tools are loaded.

### **Step 2: Run the MCP Server**
Once testing is successful, start the actual MCP server using the command below:
```bash
uv run fastmcp run main.py
```
This runs your custom MCP server and makes it available for clients like Claude Desktop to connect.

### **Step 3: Install Custom MCP Server to Claude Desktop**
Install your custom MCP server into Claude Desktop using the following command:
```bash
uv run fastmcp install claude-desktop main.py
```
This automatically updates Claude’s MCP configuration to include your server.

### **Step 4: Verify Configuration in Claude Desktop**
Locate the Claude Desktop MCP configuration file (usually located under
C:\\Users\\<username>\\AppData\\Roaming\\Claude\\mcp.json) and ensure it includes an entry similar to the one below:
```bash
{
  "CoinGeckoMCP": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp",
      "fastmcp",
      "run",
      "C:\\\\Users\\\\91861\\\\OneDrive\\\\Desktop\\\\COURSES\\\\MCP\\\\Crypto-Currency-MCP-Server\\\\main.py"
    ],
    "env": {},
    "transport": "stdio",
    "type": null,
    "cwd": null,
    "timeout": null,
    "description": null,
    "icon": null,
    "authentication": null
  }
}
```
Ensure that the main.py path points to your MCP server file location.

### **Step 5: Restart Claude Desktop**
After confirming the configuration:
- Close Claude Desktop completely.
- Restart it.
Claude should now detect and connect to your custom CoinGecko MCP Server automatically.
