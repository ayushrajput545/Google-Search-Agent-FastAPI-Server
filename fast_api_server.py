from fastapi import FastAPI , HTTPException
from langserve import add_routes
from agent import agent
from pydantic import BaseModel


app = FastAPI(
    title="Google Search Agent" #optional
)

@app.get('/health')
def Health():
    return {"Status":"Ok"}

# add_routes( #http://127.0.0.1:8000/docs?utm_source=chatgpt.com#/ 
#     app,
#     agent,
#     path="/search-agent"
# )

# NO Langserve: Pure fast api 

class SearchRequest(BaseModel):
    query:str

@app.post('/search')
async def search(request:SearchRequest):
    try:
        result = await agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": request.query
                }
            ]
        })

        answer = result["messages"][-1].content

        return {
            "query": request.query,
            "answer": answer
        }

    except Exception as e:
        print(f"Agent error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Agent execution failed"
        )



# fastapi run fast_apis.py