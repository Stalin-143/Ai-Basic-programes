using Flux
using CSV
using DataFrames
using Plots
using Statistics

# Load and preprocess the dataset
data_file = "stock_prices.csv"  # Replace with your CSV file containing stock prices
data = CSV.read(data_file, DataFrame)

# Assuming the CSV has a column "Close" for closing prices
prices = data.Close

# Normalize the data
function normalize(data)
    return (data .- mean(data)) ./ std(data)
end

normalized_prices = normalize(prices)

# Prepare the dataset for training
function prepare_data(data, seq_len)
    X, Y = [], []
    for i in 1:(length(data) - seq_len)
        push!(X, data[i:i+seq_len-1])
        push!(Y, data[i+seq_len])
    end
    return hcat(X...)', hcat(Y...)
end

seq_len = 50  # Sequence length for LSTM
X, Y = prepare_data(normalized_prices, seq_len)

# Split into training and test sets
train_ratio = 0.8
train_size = Int(floor(train_ratio * size(X, 1)))

X_train, X_test = X[1:train_size, :], X[train_size+1:end, :]
Y_train, Y_test = Y[1:train_size], Y[train_size+1:end]

# Convert to Flux tensors
X_train = Flux.unsqueeze(Float32.(X_train), dims=3)
X_test = Flux.unsqueeze(Float32.(X_test), dims=3)
Y_train = Float32.(Y_train)
Y_test = Float32.(Y_test)

# Define the LSTM model
model = Chain(
    LSTM(seq_len, 50),
    Dense(50, 1)
)

# Define loss function and optimizer
loss(x, y) = Flux.mse(model(x), y)
opt = ADAM(0.001)

# Training the model
function train!(epochs)
    for epoch in 1:epochs
        for i in 1:train_size
            Flux.train!(loss, params(model), [(X_train[:, :, i], Y_train[i])], opt)
        end
        println("Epoch $epoch: Training Loss = $(loss(X_train, Y_train))")
    end
end

train!(50)  # Train for 50 epochs

# Test the model
predictions = model(X_test)

# Plot the results
plot(1:length(Y_test), Y_test, label="Actual")
plot!(1:length(predictions), predictions, label="Predicted", linestyle=:dash)

# Save the model
Flux.save("stock_price_predictor.bson", model)
