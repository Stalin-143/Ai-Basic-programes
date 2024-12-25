# Requires: OpenAI API key
# Save this script as `StoryAI.ps1` and run in PowerShell.

# Define API Key and URL
$apiKey = "YOUR_OPENAI_API_KEY"
$apiUrl = "https://api.openai.com/v1/completions"

# Prompt for story idea
$prompt = @"
You are an AI assistant designed to create engaging story ideas. 
Please write a short outline for a story based on the user's genre and theme preferences.
"@

# User Input: Genre and Theme
$genre = Read-Host "Enter the story genre (e.g., fantasy, sci-fi, thriller)"
$theme = Read-Host "Enter the story theme (e.g., overcoming fears, friendship, revenge)"

# Final Story Prompt
$finalPrompt = "$prompt The genre is $genre, and the theme is $theme."

# Prepare API Request Body
$requestBody = @{
    model = "text-davinci-003"
    prompt = $finalPrompt
    max_tokens = 500
    temperature = 0.7
} | ConvertTo-Json -Depth 10

# Send Request to OpenAI
try {
    $response = Invoke-RestMethod -Uri $apiUrl -Method Post -Headers @{
        "Authorization" = "Bearer $apiKey"
        "Content-Type"  = "application/json"
    } -Body $requestBody

    # Output the Story Idea
    Write-Host "`nGenerated Story Idea:`n" -ForegroundColor Green
    Write-Host $response.choices.text.Trim()
} catch {
    Write-Host "Error: Could not connect to the OpenAI API." -ForegroundColor Red
}
