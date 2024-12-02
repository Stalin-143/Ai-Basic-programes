# PowerShell Script: Basic AI with REST API

# Define API endpoint and key (replace with your actual endpoint and API key)
$endpoint = "https://<your-endpoint>.cognitiveservices.azure.com/text/analytics/v3.0/sentiment"
$apiKey = "<your-api-key>"

# Input text for sentiment analysis
$text = Read-Host "Enter the text you want to analyze for sentiment"

# Prepare the JSON payload
$body = @{
    documents = @(
        @{
            id = "1";
            language = "en";
            text = $text
        }
    )
} | ConvertTo-Json -Depth 10

# Set headers
$headers = @{
    "Ocp-Apim-Subscription-Key" = $apiKey
    "Content-Type" = "application/json"
}

# Make the REST API call
$response = Invoke-RestMethod -Uri $endpoint -Method Post -Body $body -Headers $headers

# Display the results
if ($response) {
    $sentiment = $response.documents[0].sentiment
    $confidence = $response.documents[0].confidenceScores

    Write-Host "Sentiment Analysis Results:" -ForegroundColor Green
    Write-Host "  Sentiment: $sentiment"
    Write-Host "  Positive Confidence: $($confidence.positive)"
    Write-Host "  Neutral Confidence: $($confidence.neutral)"
    Write-Host "  Negative Confidence: $($confidence.negative)"
} else {
    Write-Host "Error: No response from the API" -ForegroundColor Red
}
