
import uvicorn
from app.mcp.mcp_server import WashingMachineMCPServer

if __name__ == "__main__":
    mcp = WashingMachineMCPServer()
    uvicorn.run(mcp.app, host="0.0.0.0", port=8000)
