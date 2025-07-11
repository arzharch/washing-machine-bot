import asyncio
from app.mcp.mcp_server import WashingMachineMCPServer

async def test_create_ticket():
    server = WashingMachineMCPServer()
    result = await server.create_ticket({
        "title": "CLI Direct Test Ticket",
        "description": "Machine making loud noise during spin cycle.",
        "phone_number": "+11234567890",
        "priority": "high"
    })
    print("Result:", result)

if __name__ == "__main__":
    asyncio.run(test_create_ticket())
