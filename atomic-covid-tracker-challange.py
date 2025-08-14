# atomic_covid_tracker.py - COVID-19 Global Data Tracker (Shadow Garden Edition)

# Importing necessary modules for our mission
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px # For advanced global intel mapping

print("--- Initiating COVID-19 Global Data Tracker (Shadow Garden Edition) ---")
print("Objective: Acquire, Process, Analyze, and Visualize Global Health Intelligence.")
print("Priority Target: South Africa's Tactical Data.")
print("-------------------------------------------------------------------")

# --- 1️⃣ Data Collection & Loading ---
print("\n[Phase 1: Data Acquisition & Initial Reconnaissance]")

# Action: Data will now be retrieved directly from the online URL.
# URL: https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv
covid_data_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv' # Changed to online URL

try:
    print(f"📡 Attempting to load global intel from '{covid_data_url}'...")
    df = pd.read_csv(covid_data_url)
    print("✅ Global Intel Dataset Loaded Successfully. Data stream established. ✅")

    # Check columns
    print("\n📦 Data Schema Overview (df.columns):")
    print(df.columns.tolist())

    # Preview rows
    print("\n📦 First 5 Tactical Data Rows (df.head()):")
    print(df.head())

    # Identify missing values
    print("\n🔍 Missing Intel Scan (df.isnull().sum()):")
    print(df.isnull().sum()[df.isnull().sum() > 0]) # Only show columns with missing values

except FileNotFoundError: # This error is less likely with URL, but kept for general robustness
    print(f"\n🚨 ERROR: Intel source '{covid_data_url}' not found. Verify URL or network connection. 🚨")
    print("Protocol halted. Cannot proceed without raw data feed.")
    exit() # Exit the program if the file isn't found
except pd.errors.EmptyDataError:
    print(f"\n🚨 ERROR: No data found at '{covid_data_url}'. The online source might be empty or malformed. 🚨")
    print("Protocol halted.")
    exit()
except pd.errors.ParserError:
    print(f"\n🚨 ERROR: Failed to parse data from '{covid_data_url}'. Data format might be incorrect. 🚨")
    print("Protocol halted.")
    exit()
except Exception as e:
    print(f"\n🚨 CRITICAL ERROR during data acquisition: {e}. Protocol Halted. Check network connection or URL validity. �")
    exit()

print("-------------------------------------------------------------------")

# --- 2️⃣ Data Cleaning ---
print("\n[Phase 2: Data Purification Protocol]")

# Convert date column to datetime
print("🧹 Converting 'date' column to Datetime format for temporal analysis...")
df['date'] = pd.to_datetime(df['date'])
print("✅ Date column converted. Temporal clarity achieved. ✅")

# Filter countries of interest (including South Africa as primary target)
# Key columns for analysis
required_columns = [
    'date', 'location', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
    'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
    'population', 'stringency_index', 'continent', 'iso_code'
]
# Ensure required columns exist before filtering
df = df[df.columns.intersection(required_columns)]

# Countries of interest, with South Africa as the primary focus
countries_of_interest = ['South Africa', 'United States', 'India', 'United Kingdom', 'Brazil']
df_filtered = df[df['location'].isin(countries_of_interest)].copy() # Use .copy() to avoid SettingWithCopyWarning

# Drop rows with missing dates/critical values (e.g., total_cases, population for our selected countries)
print("\n🧹 Dropping rows with missing critical intel (cases/population)...")
initial_rows_filtered = df_filtered.shape[0]
df_filtered.dropna(subset=['total_cases', 'population'], inplace=True)
cleaned_rows_filtered = df_filtered.shape[0]
print(f"Report: Removed {initial_rows_filtered - cleaned_rows_filtered} incomplete intel entries.")
print("✅ Critical missing data handled. ✅")

# Handle missing numeric values with fillna() or interpolate().
# For vaccination data, interpolation is often better for trends.
print("\n🧹 Interpolating missing numerical data points for smooth trend analysis...")
numeric_cols_to_fill = ['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'new_cases', 'new_deaths']
for col in numeric_cols_to_fill:
    if col in df_filtered.columns:
        df_filtered[col] = df_filtered.groupby('location')[col].transform(lambda x: x.interpolate(method='linear', limit_direction='both'))
        # After interpolation, fill any remaining NaNs (e.g., at ends) with 0 if that's appropriate for metrics.
        df_filtered[col] = df_filtered[col].fillna(0)
        # Ensure positive values, as some data might be negative after interpolation or initial errors
        df_filtered[col] = df_filtered[col].apply(lambda x: max(0, x))

print("✅ Numerical data interpolation complete. Trends smoothed. ✅")
print("\n📦 Filtered and Cleaned Data Sample (df_filtered.head()):")
print(df_filtered.head())
print("-------------------------------------------------------------------")

# --- 3️⃣ Exploratory Data Analysis (EDA) ---
print("\n[Phase 3: Tactical Data Analysis & Insight Generation]")

# Calculate the death rate: total_deaths / total_cases.
print("📊 Calculating Death Rate (Mortal Coil Index)...")
df_filtered['death_rate'] = (df_filtered['total_deaths'] / df_filtered['total_cases']) * 100
df_filtered['death_rate'] = df_filtered['death_rate'].fillna(0) # Handle division by zero for 0 cases
df_filtered['death_rate'] = df_filtered['death_rate'].replace([float('inf'), -float('inf')], 0) # Replace inf with 0
print("✅ Mortal Coil Index computed. Vulnerability identified. ✅")

# Compute basic statistics of numerical columns
print("\n📊 Core Metrics Overview (df_filtered.describe()):")
print(df_filtered.describe())

# Set Matplotlib/Seaborn style for atomic visualizations
sns.set_style("darkgrid")
plt.rcParams.update({
    "figure.facecolor": "#1a202c",
    "axes.facecolor": "#2d3748",
    "text.color": "#e2e8f0",
    "axes.labelcolor": "#a0aec0",
    "xtick.color": "#a0aec0",
    "ytick.color": "#a0aec0",
    "grid.color": "#4a5568",
    "axes.edgecolor": "#805ad5",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.family": ["DejaVu Sans", "sans-serif"], # Using generic font for compatibility
    "legend.edgecolor": "#5a6a7c"
})

# ✅ Visualizations:

# Line chart: Plot total cases over time for selected countries.
print("\nGenerating Visualizations: Total Cases Over Time...")
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='location', palette='viridis', linewidth=2.5)
plt.title('Total Confirmed Cases Over Time by Location (Global Contagion Trajectory) 📈', fontsize=18, color='#c3a6ff')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Total Cases', fontsize=14)
plt.yscale('log') # Use log scale for better visibility of early trends
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Location', title_fontsize='13', fontsize='11', loc='upper left')
plt.tight_layout()
plt.show()

# Line chart: Plot total deaths over time.
print("Generating Visualizations: Total Deaths Over Time...")
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_filtered, x='date', y='total_deaths', hue='location', palette='magma', linewidth=2.5)
plt.title('Total Deaths Over Time by Location (Mortal Coil Progression) 💀', fontsize=18, color='#c3a6ff')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Total Deaths', fontsize=14)
plt.yscale('log')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Location', title_fontsize='13', fontsize='11', loc='upper left')
plt.tight_layout()
plt.show()

# Compare daily new cases between countries (example for a specific period or overall)
print("Generating Visualizations: Daily New Cases Comparison...")
# Take a rolling average to smooth out daily fluctuations for better trend visualization
df_filtered['new_cases_smoothed'] = df_filtered.groupby('location')['new_cases'].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_filtered, x='date', y='new_cases_smoothed', hue='location', palette='plasma', linewidth=2.5)
plt.title('Daily New Cases (7-Day Smoothed) Over Time (Infection Sprawl Dynamics) 📊', fontsize=18, color='#c3a6ff')
plt.xlabel('Date', fontsize=14)
plt.ylabel('7-Day Avg New Cases', fontsize=14)
plt.yscale('log') # Use log scale if new cases vary widely
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Location', title_fontsize='13', fontsize='11', loc='upper left')
plt.tight_layout()
plt.show()

# Bar chart: Top countries by total cases (latest date)
print("Generating Visualizations: Top Countries by Total Cases (Latest Intel)...")
latest_data = df_filtered.loc[df_filtered.groupby('location')['date'].idxmax()]
latest_data_sorted = latest_data.sort_values('total_cases', ascending=False)

plt.figure(figsize=(12, 7))
sns.barplot(x='location', y='total_cases', data=latest_data_sorted, palette='rocket')
plt.title('Total Cases by Location (Latest Global Contagion Status) 🌍', fontsize=18, color='#c3a6ff')
plt.xlabel('Location', fontsize=14)
plt.ylabel('Total Cases', fontsize=14)
plt.ticklabel_format(style='plain', axis='y') # Prevent scientific notation on y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Histogram of a numerical column to understand its distribution (e.g., New Cases in South Africa)
print("Generating Visualizations: New Cases Distribution in South Africa...")
sa_data = df_filtered[df_filtered['location'] == 'South Africa'].copy()
plt.figure(figsize=(10, 6))
sns.histplot(sa_data['new_cases'], bins=30, kde=True, color='#6b46c1')
plt.title('Distribution of Daily New Cases in South Africa (SA Infection Frequency) 🇿🇦', fontsize=16, color='#c3a6ff')
plt.xlabel('Daily New Cases', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print("-------------------------------------------------------------------")

# --- 4️⃣ Visualizing Vaccination Progress ---
print("\n[Phase 4: Vaccination Rollout Analysis]")

# Plot cumulative vaccinations over time for selected countries.
print("Generating Visualizations: Cumulative Vaccinations Over Time...")
plt.figure(figsize=(14, 8))
# Filter out locations with no vaccination data if necessary
vaccine_data = df_filtered.dropna(subset=['total_vaccinations'])
if not vaccine_data.empty:
    sns.lineplot(data=vaccine_data, x='date', y='total_vaccinations', hue='location', palette='crest', linewidth=2.5)
    plt.title('Cumulative Vaccinations Over Time by Location (Global Immunization Trajectory) 💉', fontsize=18, color='#c3a6ff')
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Total Vaccinations', fontsize=14)
    plt.yscale('log') # Log scale for better trend visualization
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='Location', title_fontsize='13', fontsize='11', loc='upper left')
    plt.tight_layout()
    plt.show()
else:
    print("Warning: No sufficient vaccination data for selected locations to plot cumulative vaccinations.")


# Compare % vaccinated population (using 'people_vaccinated_per_hundred' if available, or calculate)
# The OWID dataset often provides 'people_vaccinated_per_hundred' and 'people_fully_vaccinated_per_hundred'
# Let's use 'people_fully_vaccinated_per_hundred' as a robust metric.
print("Generating Visualizations: Fully Vaccinated Population Percentage...")
latest_vaccination_data = df_filtered.loc[df_filtered.groupby('location')['date'].idxmax()]
# Ensure the column exists and has non-zero population for division
if 'people_fully_vaccinated_per_hundred' in latest_vaccination_data.columns:
    latest_vaccination_data = latest_vaccination_data.dropna(subset=['people_fully_vaccinated_per_hundred'])
    latest_vaccination_data_sorted = latest_vaccination_data.sort_values('people_fully_vaccinated_per_hundred', ascending=False)
    
    if not latest_vaccination_data_sorted.empty:
        plt.figure(figsize=(12, 7))
        sns.barplot(x='location', y='people_fully_vaccinated_per_hundred', data=latest_vaccination_data_sorted, palette='rocket_r')
        plt.title('Percentage of Population Fully Vaccinated (Global Immunity Index) 🛡️', fontsize=18, color='#c3a6ff')
        plt.xlabel('Location', fontsize=14)
        plt.ylabel('Fully Vaccinated (% of Population)', fontsize=14)
        plt.ylim(0, 100) # Percentage scale
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    else:
        print("Warning: No sufficient 'people_fully_vaccinated_per_hundred' data for selected locations to plot.")
else:
    print("Warning: 'people_fully_vaccinated_per_hundred' column not found or is empty.")

print("-------------------------------------------------------------------")

# --- 5️⃣ Optional: Build a Choropleth Map ---
print("\n[Phase 5: Global Tactical Mapping (Choropleth)]")

# Prepare a dataframe with iso_code, total_cases for the latest date.
# Filter for the latest date for each country for the map
map_data = df.loc[df.groupby('iso_code')['date'].idxmax()]
# Ensure we only include countries with 'total_cases' and 'iso_code'
map_data = map_data.dropna(subset=['iso_code', 'total_cases'])

if not map_data.empty:
    print("Generating Global Contagion Map...")
    fig = px.choropleth(map_data,
                        locations="iso_code",
                        color="total_cases",
                        hover_name="location",
                        color_continuous_scale=px.colors.sequential.Plasma, # Atomic plasma color scale
                        title='Global Total COVID-19 Cases (Latest Tactical Overview) 🗺️',
                        labels={'total_cases':'Total Cases'},
                        projection="natural earth")
    fig.update_layout(
        paper_bgcolor="#1a202c",  # Dark background
        font_color="#e2e8f0",      # Light text color
        title_font_color="#c3a6ff", # Atomic title color
        geo_bgcolor="#2d3748"      # Darker map background
    )
    fig.show()
    print("✅ Global Contagion Map projected. Threat assessment refined. ✅")
else:
    print("Warning: Not enough data to generate a Global Contagion Map.")

print("-------------------------------------------------------------------")

# --- 6️⃣ Insights & Reporting ---
print("\n[Phase 6: Strategic Insights & Final Report]")

print("📝 Final Tactical Report - Key Atomic Insights:")

print("1. **Global Contagion Acceleration (📈):** The total cases and deaths exhibit exponential growth patterns across major locations, especially in early phases. The log scale visualization clearly shows initial rapid proliferation, signifying the virus's inherent atomic spread capability.")
print("2. **Divergent Immunization Strategies (💉):** While vaccination efforts are evident across all tracked locations, the pace and total coverage vary significantly. Some locations achieved high vaccination percentages relatively quickly, indicating robust logistical atomic precision in rollout campaigns.")
print("3. **South Africa's Resilience and Unique Trajectory (🇿🇦):** Our analysis highlights South Africa (SA) as a critical data point. While SA faced substantial waves, its daily new cases distribution shows a complex pattern, indicating a dynamic response and potentially unique epidemiological factors or data reporting nuances. Its vaccination rollout, when visualized comparatively, reveals specific phases of acceleration and stabilization unique to the region's operational environment.")
print("4. **Death Rate Refinement (💀):** The calculated death rate (Total Deaths / Total Cases) provides a more nuanced understanding of the pandemic's lethality per confirmed infection, varying between locations. This 'Mortal Coil Index' is crucial for assessing the true impact of the viral entity.")
print("5. **Inter-Component Correlations (🧬):** The relationship between different metrics, such as higher total cases often correlating with higher death counts, confirms expected tactical dependencies. The choropleth map provides a stark visual summary of global contagion density, pinpointing high-impact zones for future surveillance.")

print("\n--- COVID-19 Data Intelligence Protocol Complete. Mission Accomplished. 🌙 ---")
print("Thank you for using the COVID-19 Global Data Tracker (Shadow Garden Edition). Stay vigilant and informed.")
print("For further analysis or data requests, please contact the Shadow Garden Data Operations Center.")
print("-------------------------------------------------------------------")
# End of atomic_covid_tracker.py