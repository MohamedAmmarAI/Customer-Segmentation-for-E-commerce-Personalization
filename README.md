
# Customer Segmentation

This project leverages K-means clustering and Principal Component Analysis (PCA) to perform customer segmentation based on purchasing behavior in an e-commerce dataset. The primary goal is to discover distinct groups of customers with similar preferences and behaviors, enabling personalized marketing strategies and recommendations.

---

## Project Overview
E-commerce businesses aim to understand their customers to deliver tailored experiences. Using unsupervised learning techniques such as K-means clustering combined with PCA, this project segments customers into meaningful groups based on their purchasing behaviors. These segments enable businesses to implement targeted marketing campaigns and improve customer satisfaction.

---

## Dataset Information
The project utilizes the **Online Retail Dataset** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail). This dataset contains transactional data from an e-commerce retailer, including fields like:
- Invoice number
- Stock code
- Quantity
- Customer ID
- Purchase date
- Unit price

---

## Methodology

### 1. Data Preparation
- **Dataset Preprocessing**: Handle missing values, clean irrelevant data, and prepare the dataset for analysis.
- **Feature Transformation**: Transform raw data into features such as purchase history, order frequency, total spending, recency of purchase, and average basket size.

### 2. Feature Engineering
Relevant customer behavior metrics are extracted to reflect purchasing habits. Additional metrics may include:
- Recency
- Frequency
- Monetary (RFM) features

### 3. Dimensionality Reduction
PCA is applied to:
- Reduce dimensionality.
- Retain the most informative features.
- Highlight underlying patterns.

### 4. Determining Optimal Number of Clusters
Techniques used:
- **Elbow Method**: Analyze within-cluster sum of squares (WCSS).
- **Silhouette Analysis**: Measure the quality of clusters for different values of K.

### 5. K-means Clustering
Clusters are generated to group customers based on their feature values, creating distinct customer segments.

### 6. Cluster Profiling
Clusters are profiled by calculating metrics like:
- Average spending
- Purchase frequency
- Popular product categories

### 7. Visualization
Visualization techniques such as scatter plots are used to:
- Depict customer clusters in the reduced feature space.
- Illustrate distinctions between clusters.

### 8. Evaluation
Metrics used for evaluation include:
- Silhouette Score
- Within-cluster sum of squares (WCSS)

### 9. Personalization and Recommendations
Customized marketing strategies are devised for each segment, enhancing:
- Promotions
- Product recommendations
- Customer engagement

---

## Results and Insights
- Identified X distinct customer segments.
- Highlighted customer behaviors such as high-value buyers or infrequent purchasers.
- Insights provide actionable strategies for:
  - Targeted marketing campaigns.
  - Enhanced customer retention.
  - Inventory optimization.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MohamedAmmarAI/Customer-Segmentation-for-E-commerce-Personalization.git
