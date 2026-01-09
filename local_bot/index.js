const { Client, LocalAuth } = require('whatsapp-web.js');
const { generate } = require('qrcode-terminal');
const { post } = require('axios');

// Initialize WhatsApp Client
const client = new Client({
    authStrategy: new LocalAuth(), // Saves your session so you don't scan QR every time
    puppeteer: {
        args: ['--no-sandbox'], // Required for many Linux/WSL environments
    }
});

// Display QR Code for login
client.on('qr', (qr) => {
    console.log('Scan this QR code with your WhatsApp:');
    generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('HardDevs Bot is online and ready!');
});

// Main message listener
client.on('message', async (msg) => {
    const messageBody = msg.body.toLowerCase();

    // Check if the bot is mentioned
    if (messageBody.includes('@harddevs-bot')) {
        console.log(`Received message from ${msg.from}: ${msg.body}`);

        // Remove the tag from the prompt
        const cleanPrompt = msg.body.replace(/@harddevs-bot/gi, '').trim();

        try {
            // Call local Ollama API
            const response = await post('http://localhost:11434/api/generate', {
                model: 'harddevs-bot',
                prompt: cleanPrompt,
                stream: false // We want the full response at once
            });

            const botReply = response.data.response;
            
            // Send the reply back to WhatsApp
            msg.reply(botReply);

        } catch (error) {
            console.error('Error calling Ollama:', error.message);
            msg.reply('Mielda manín, se me fundieron los plomos. Intenta de nuevo ahorita.');
        }
    }
    else {
        console.log(`Ignored message from ${msg.from}: ${msg.body}`);
    }
});

client.initialize();
