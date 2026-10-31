# First MCP Server

This project is a beginner-friendly implementation of a Model Context Protocol (MCP) server. It demonstrates how to expose tools to an MCP client and how to wire up a basic server that can be used with AI-powered development tools or local clients.

## What is MCP?

The Model Context Protocol (MCP) is a standard for connecting AI applications to external tools and data sources. With MCP, an AI client can discover and invoke tools exposed by a server in a structured way.

This project serves as a practical starting point for learning how MCP servers are built and how tools are registered.

## Features

- Minimal MCP server setup
- Example tool registration
- Easy to extend with more tools
- Suitable for learning and experimentation
- Works as a starting point for custom MCP integrations

## Project Structure

```text
first-mcp-server/
├── package.json
├── src/
│   └── index.js
├── README.md
└── ...
```

## Prerequisites

Before running this project, make sure you have:

- Node.js installed (preferably v18 or later)
- npm or yarn
- A compatible MCP client or testing tool

## Installation

```bash
npm install
```

## Running the Server

```bash
node src/index.js
```

If your project uses a different start command, update as needed.

## Example Usage

Once the server is running, it can expose tools to an MCP-compatible client. The client can then discover available tools and call them using the MCP protocol.

## Extending the Server

To add more functionality:

1. Register a new tool in the server setup.
2. Define the tool input schema.
3. Implement the tool handler.
4. Test it through an MCP client.

## Learning Goals

This project is intended to help you understand:

- how an MCP server is structured
- how tools are declared and exposed
- how clients communicate with the server
- how to build your own local tool integrations

## Notes

This is a simple first project meant for learning and experimentation. It can be expanded into a more advanced server with real integrations, authentication, and production-grade tooling.

## License

This project is provided for educational purposes. Add a license if you plan to publish or share it publicly.
