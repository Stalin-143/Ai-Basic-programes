# Load necessary library
library(ggplot2)

# Load dataset
data("mtcars")

# Train a linear regression model
model <- lm(mpg ~ hp, data = mtcars)

# Display model summary
summary(model)

# Predict mpg for a car with 150 horsepower
new_data <- data.frame(hp = 150)
predicted_mpg <- predict(model, new_data)

cat("Predicted MPG for 150 horsepower:", predicted_mpg, "\n")

# Plot the data and regression line
ggplot(mtcars, aes(x = hp, y = mpg)) +
  geom_point() +
  geom_smooth(method = "lm", col = "blue") +
  labs(title = "Linear Regression: MPG vs Horsepower",
       x = "Horsepower",
       y = "Miles Per Gallon (MPG)")
