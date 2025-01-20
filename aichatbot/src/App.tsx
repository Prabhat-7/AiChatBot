import { useState } from "react";
import "./App.css";

export default function App() {
  const [messages, setmessages] = useState<string[]>([]);
  const [newMessage, setMessage] = useState("");

  async function handleSubmit() {
    setmessages((prev) => [...prev, newMessage]);
    setMessage("");
    try {
      const response = await fetch("http://127.0.0.1:8000/ask/", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(newMessage),
      });
      const answer = await response.json();
      setmessages((prev) => [...prev, answer.response]);
    } catch (e) {
      console.log(e);
    }
  }
  return (
    <>
      <header>AI CHATBOT</header>
      <div className="app-container">
        <ul>
          {messages.map((message, index) => (
            <li key={index}>{message}</li>
          ))}
        </ul>
      </div>
      <div className="input-container">
        <input
          value={newMessage}
          onChange={(e) => setMessage(e.target.value)}
          type="text"
          name=""
          id=""
          placeholder="Enter a promt"
        />
        <button onClick={handleSubmit}>
          <i className="bi bi-send-fill"></i>
        </button>
      </div>
    </>
  );
}
