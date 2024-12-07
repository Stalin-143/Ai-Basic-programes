# Install necessary libraries
install.packages(c("ggplot2", "dplyr", "cluster", "factoextra", "caret"))
library(ggplot2)
library(dplyr)
library(cluster)
library(factoextra)
library(caret)

# AI-driven Object Analysis Function
object_analysis_with_ai <- function(obj) {
  
  # Step 1: Class and Basic Structure
  cat("Class of the object:", class(obj), "\n")
  cat("Object structure:\n")
  str(obj)
  
  # Step 2: If object is a Data Frame, proceed with analysis
  if (is.data.frame(obj)) {
    cat("Number of rows:", nrow(obj), "\n")
    cat("Number of columns:", ncol(obj), "\n")
    cat("Column names:", colnames(obj), "\n")
    
    # Step 3: Descriptive statistics for numeric columns
    cat("\nDescriptive statistics for numeric columns:\n")
    summary(obj)
    
    # Step 4: Correlation matrix (for numeric columns)
    cat("\nCorrelation matrix:\n")
    print(cor(obj[sapply(obj, is.numeric)]))
    
    # Step 5: Visualizing the data with pair plots
    cat("\nVisualizing pair plots of numeric columns:\n")
    pairs(obj[sapply(obj, is.numeric)], main = "Pair Plot of Numeric Columns")
    
    # Step 6: Clustering using K-means (AI technique)
    cat("\nPerforming K-means clustering (k = 3):\n")
    kmeans_result <- kmeans(obj[sapply(obj, is.numeric)], centers = 3)
    print(kmeans_result$centers)  # Displaying the cluster centers
    cat("\nCluster assignment for first few rows:\n")
    print(kmeans_result$cluster[1:10])  # Cluster assignments for first 10 rows
    
    # Step 7: Visualizing clusters
    fviz_cluster(kmeans_result, data = obj[sapply(obj, is.numeric)], main = "K-means Clustering")

    # Step 8: Dimensionality Reduction using PCA (Principal Component Analysis)
    cat("\nPerforming PCA for dimensionality reduction:\n")
    pca_result <- prcomp(obj[sapply(obj, is.numeric)], scale. = TRUE)
    summary(pca_result)  # Variance explained by each principal component
    
    # Plotting PCA results
    pca_data <- data.frame(pca_result$x)
    ggplot(pca_data, aes(PC1, PC2)) +
      geom_point() +
      ggtitle("PCA Plot: First vs Second Principal Component")
  }
  
  # Step 9: If the object is a list, analyze the components
  else if (is.list(obj)) {
    cat("\nObject is a list. Analyzing components:\n")
    lapply(obj, function(x) {
      cat("\nClass of component:", class(x), "\n")
      str(x)
    })
  }
  
  # Step 10: If object is a vector
  else if (is.vector(obj)) {
    cat("\nLength of vector:", length(obj), "\n")
    cat("First few elements of the vector:\n")
    print(head(obj))
  }
}

# Example: Load the iris dataset and analyze it
data(iris)
object_analysis_with_ai(iris)
