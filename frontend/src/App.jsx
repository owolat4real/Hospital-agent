import { useState } from "react";
 
function App() {
 
  const [message, setMessage] = useState("");

  const [chat, setChat] = useState([]);
 
  const sendMessage = async () => {
 
    if (!message) return;
 
    const userMessage = {

      role: "user",

      content: message

    };
 
    setChat((prev) => [...prev, userMessage]);
 
    try {
 
      // Example:

      // "analyze 1"
 
      const patientId = message.split(" ")[1];
 
      const response = await fetch(

        `http://127.0.0.1:8000/analyze/${patientId}`

      );
 
      const data = await response.json();
 
      const aiMessage = {

        role: "assistant",

        content: JSON.stringify(data, null, 2)

      };
 
      setChat((prev) => [

        ...prev,

        aiMessage

      ]);
 
    } catch (error) {
 
      const errorMessage = {

        role: "assistant",

        content: "Error connecting to backend"

      };
 
      setChat((prev) => [

        ...prev,

        errorMessage

      ]);

    }
 
    setMessage("");

  };
 
  return (
 
    <div

      style={{

        maxWidth: "800px",

        margin: "auto",

        padding: "20px",

        fontFamily: "Arial"

      }}
>
 
      <h1>AI Hospital Assistant</h1>
 
      <div

        style={{

          border: "1px solid gray",

          height: "500px",

          overflowY: "auto",

          padding: "20px",

          marginBottom: "20px"

        }}
>
 
        {chat.map((msg, index) => (
 
          <div

            key={index}

            style={{

              marginBottom: "20px",

              textAlign:

                msg.role === "user"

                  ? "right"

                  : "left"

            }}
>
 
            <div

              style={{

                display: "inline-block",

                padding: "10px",

                borderRadius: "10px",

                background:

                  msg.role === "user"

                    ? "#007bff"

                    : "#f1f1f1",

                color:

                  msg.role === "user"

                    ? "white"

                    : "black",

                maxWidth: "70%"

              }}
>
 
              <pre

                style={{

                  whiteSpace: "pre-wrap"

                }}
>

                {msg.content}
</pre>
 
            </div>
 
          </div>
 
        ))}
 
      </div>
 
      <div

        style={{

          display: "flex",

          gap: "10px"

        }}
>
 
        <input

          type="text"

          placeholder="Type: analyze 1"

          value={message}

          onChange={(e) =>

            setMessage(e.target.value)

          }

          style={{

            flex: 1,

            padding: "10px"

          }}

        />
 
        <button

          onClick={sendMessage}

          style={{

            padding: "10px 20px"

          }}
>

          Send
</button>
 
      </div>
 
    </div>

  );

}
 
export default App;
 