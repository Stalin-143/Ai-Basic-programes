import Foundation

// Define the API endpoint and your API key
let apiKey = "your_openai_api_key"
let url = URL(string: "https://api.openai.com/v1/chat/completions")!

// Create the headers for the API request
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.setValue("Bearer \(apiKey)", forHTTPHeaderField: "Authorization")

// Define the request body
let requestBody: [String: Any] = [
    "model": "gpt-3.5-turbo", // or you can use "gpt-4" if preferred
    "messages": [
        ["role": "system", "content": "You are a helpful assistant."],
        ["role": "user", "content": "Hello!"]
    ]
]

do {
    let jsonData = try JSONSerialization.data(withJSONObject: requestBody)
    request.httpBody = jsonData
} catch {
    print("Error serializing JSON: \(error)")
}

// Make the API request
let task = URLSession.shared.dataTask(with: request) { data, response, error in
    if let error = error {
        print("Error making request: \(error)")
        return
    }
    
    if let data = data {
        do {
            // Parse the response
            if let jsonResponse = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any],
               let choices = jsonResponse["choices"] as? [[String: Any]],
               let firstChoice = choices.first,
               let message = firstChoice["message"] as? [String: Any],
               let content = message["content"] as? String {
                // Print the response from the chatbot
                print("Chatbot Response: \(content)")
            }
        } catch {
            print("Error parsing JSON response: \(error)")
        }
    }
}

task.resume()
