chatBot <- function() {
  cat("Hello! I'm your R chatbot. Type 'bye' to exit.\n")

  repeat {
    cat("You: ")
    userInput <- tolower(trimws(readline()))

    if (userInput == "bye") {
      cat("ChatBot: Goodbye! Have a great day!\n")
      break
    } else {
      response <- respond(userInput)
      cat("ChatBot: ", response, "\n")
    }
  }
}

respond <- function(input) {
  greetings <- c("hello", "hi", "hey", "greetings")

  if (any(greetings %in% unlist(strsplit(input, " ")))) {
    return("Hi there! How can I help you?")
  } else if (grepl("how are you", input)) {
    return("I'm just a script, but I'm here to help you!")
  } else if (grepl("help", input)) {
    return("Sure! What do you need help with?")
  } else {
    return("I'm not sure I understand that. Can you elaborate?")
  }
}

# Run the chatbot
chatBot()
