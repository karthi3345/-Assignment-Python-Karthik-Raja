async function sendChat(){

    const message=document.getElementById("chatMessage").value;

    const response=await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            message:message,

            history:[]
        })

    });

    const data=await response.json();

    document.getElementById("chatResult").innerText=data.reply;

}


async function generateImage(){

    const prompt=document.getElementById("imagePrompt").value;

    const response=await fetch("/image",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            prompt:prompt

        })

    });

    const data=await response.json();

    if(data.data){

        document.getElementById("generatedImage").src=
        "data:image/png;base64,"+data.data[0].b64_json;

    }

}


async function analyzeImage() {

    const fileInput = document.getElementById("visionImage");
    const questionInput = document.getElementById("visionQuestion");
    const resultBox = document.getElementById("visionResult");

    const file = fileInput.files[0];
    const question = questionInput.value;

    // -----------------------
    // Validation (Frontend)
    // -----------------------
    if (!file) {
        resultBox.innerText = "⚠️ Please select an image";
        return;
    }

    if (!question || question.trim() === "") {
        resultBox.innerText = "⚠️ Please enter a question";
        return;
    }

    resultBox.innerText = "⏳ Analyzing image...";

    const formData = new FormData();
    formData.append("image", file);
    formData.append("question", question);

    try {

        const response = await fetch("/vision", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log("VISION RESPONSE:", data);

        if (!response.ok) {
            resultBox.innerText = data.detail || data.error || "Vision failed";
            return;
        }

        // -----------------------
        // Flexible response handling
        // -----------------------
        const answer =
            data.answer ||
            data.reply ||
            data.message ||
            data.result ||
            JSON.stringify(data);

        resultBox.innerText = answer;

    } catch (error) {
        console.error(error);
        resultBox.innerText = "❌ Network error or server issue";
    }
}

function clearAll() {

    if (!confirm("Clear all data?")) return;

    // CHAT
    const chatMsg = document.getElementById("chatMessage");
    const chatRes = document.getElementById("chatResult");

    if (chatMsg) chatMsg.value = "";
    if (chatRes) chatRes.innerText = "";

    // IMAGE
    const imgPrompt = document.getElementById("imagePrompt");
    const img = document.getElementById("generatedImage");

    if (imgPrompt) imgPrompt.value = "";
    if (img) img.src = "";

    // VISION
    const visionImg = document.getElementById("visionImage");
    const visionQ = document.getElementById("visionQuestion");
    const visionRes = document.getElementById("visionResult");

    if (visionImg) visionImg.value = "";
    if (visionQ) visionQ.value = "";
    if (visionRes) visionRes.innerText = "";

    console.log("All cleared successfully");
}