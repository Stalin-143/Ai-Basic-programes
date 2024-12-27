       IDENTIFICATION DIVISION.
       PROGRAM-ID. CHATBOT.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 USER-INPUT           PIC X(100).
       01 RESPONSE             PIC X(100).
       PROCEDURE DIVISION.
       MAIN-LOGIC.
           DISPLAY "Welcome to the COBOL Chatbot!"
           DISPLAY "Type 'exit' to quit."
           PERFORM UNTIL USER-INPUT = "exit"
               DISPLAY "You: " WITH NO ADVANCING
               ACCEPT USER-INPUT
               EVALUATE TRUE
                   WHEN USER-INPUT = "hello"
                       MOVE "Hello! How can I help you today?" TO RESPONSE
                   WHEN USER-INPUT = "how are you"
                       MOVE "I'm just a program, but I'm functioning perfectly!" TO RESPONSE
                   WHEN USER-INPUT = "bye"
                       MOVE "Goodbye! Have a great day!" TO RESPONSE
                   WHEN OTHER
                       MOVE "I'm sorry, I didn't understand that." TO RESPONSE
               END-EVALUATE
               DISPLAY "Bot: " RESPONSE
           END-PERFORM
           DISPLAY "Chatbot session ended."
           STOP RUN.
