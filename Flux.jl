using Flux
using Statistics

# Generate some example data (y = 2x + 1)
x = rand(100)  # Random input data
y = 2 * x .+ 1 .+ 0.1 * randn(100)  # Output data with some noise

# Define the model: A simple linear layer with one input and one output
model = Chain(
    Dense(1, 1)  # Dense layer with 1 input and 1 output
)

# Loss function: Mean Squared Error (MSE)
loss(x, y) = Flux.mse(model(x), y)

# Training loop
optimizer = ADAM()  # Optimizer choice (Adam)

# Prepare the data (reshape to column vectors)
x_data = reshape(x, 100, 1)
y_data = reshape(y, 100, 1)

# Train the model
for epoch in 1:1000
    Flux.train!(loss, params(model), [(x_data, y_data)], optimizer)
    if epoch % 100 == 0
        println("Epoch $epoch, Loss: $(loss(x_data, y_data))")
    end
end

# After training, you can use the model to predict
new_x = [0.5, 1.5, 2.5]  # New input data
predictions = model(reshape(new_x, length(new_x), 1))

println("Predictions for new data: $predictions")
