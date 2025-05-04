# OIM3640FinalProject
# Vehicle Performance Analyzer

### Team Members
- Jason Park

---

## The Big Idea

### Why We Built This
Buying a car is one of the most significant financial decisions people make, yet comparing vehicles across different specifications can be overwhelming. The Vehicle Performance Analyzer solves this problem by providing a comprehensive platform that helps users make informed vehicle purchasing decisions through detailed performance specifications and side-by-side comparisons.

### The Problem We're Solving
Users interested in vehicle performance often struggle to:
- Find an easy way to compare multiple vehicles across key metrics
- Understand technical specifications like horsepower, torque, and fuel efficiency
- Determine which vehicle offers the best performance-to-price ratio
- Access centralized, reliable vehicle information in an intuitive interface

Our application addresses these pain points by centralizing vehicle information and presenting it through an intuitive, data-driven interface.

---

## Features

1. **Search Interface**
   - Find vehicles by company and model
   - Dropdown selection with 400+ vehicle models
   - Real-time model loading based on company selection

2. **Detailed Vehicle Specifications Display**
   - Horsepower and torque metrics
   - Fuel economy (city/highway MPG)
   - Transmission type and drivetrain
   - Body type and engine configuration
   - Number of cylinders and doors
   - Price ranges

3. **Side-by-Side Comparison**
   - Compare two vehicles simultaneously
   - Visual indicators highlight better values
   - Automatic performance-to-price ratio calculation
   - Color coded results for quick understanding

### Stretch Goals Implemented
1. **AI-Powered Car Buying Advisor**
   - Real-time chat interface
   - Personalized buying recommendations
   - Technical specification explanations
   - Budget and value analysis

2. **Performance-to-Price Analysis**
   - Automatic calculation of HP per $1000
   - Visual indicators for value comparison
   - Helps users identify best performance value

3. **Comprehensive Help Guide**
   - Detailed explanations of all metrics
   - Tips for effective comparison
   - Understanding visual indicators

---

## Technical Implementation

### Technology Stack
- **Backend**: Flask (Python 3.8+)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: CSV file (Car_Models.csv) - Pivoted from API Ninjas due to limitations
- **Libraries**: 
  - pandas for data processing
  - Select2 for enhanced dropdowns
  - jQuery for DOM manipulation
  - OpenAI for AI integration
- **Development**: Git version control with feature branches

### Key Implementation Details

#### 1. Data Processing
```python
# Performance metric extraction
hp_match = re.search(r'(\d+)\s*hp', car.get('Horsepower', ''))
hp = int(hp_match.group(1)) if hp_match else 0

# Performance-to-price ratio calculation
if price > 0 and hp > 0:
    car['HP per $1000'] = f"{round(hp / (price / 1000), 2)}"
```

#### 2. Comparison Algorithm
- Extracts numeric values from various text formats
- Handles different data patterns (e.g., "25 city/30 highway mpg")
- Determines better values based on metric type
- Applies visual indicators dynamically

#### 3. AI Integration
- Custom system prompt for car buying expertise
- Real-time chat processing
- Error handling for API failures
- Context-aware responses

---

### Key Pivots & Decisions
1. **API to CSV Migration**: Discovered API Ninjas limitations early (claimed to provide certain datas including fuel economy for free but does not) and pivoted to local CSV database, ensuring reliability and comprehensive data access
2. **AI Integration**: Recognized opportunity to enhance user experience with AI advisor, going beyond original MVP

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- OpenAI API key (for chatbot functionality)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/iseunpark/OIM3640FinalProject
   cd OIM3640FinalProject
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open browser and navigate to `http://127.0.0.1:5000`

---

## Results & Capabilities

### Successfully Implemented Features
1. **Efficient Vehicle Search**: Users can quickly find specific vehicles among 400+ models
2. **Comprehensive Comparison**: Side-by-side analysis of all key specifications
3. **Value Analysis**: Automatic calculation of performance-to-price ratios
4. **AI Assistance**: Real-time help for understanding specifications and making decisions
5. **Visual Clarity**: Color-coding and star indicators for quick comprehension

---

## Future Enhancements

### Database Expansion
- Integration with real-time pricing APIs
- Historical performance data
- User reviews and ratings
- Maintenance cost estimates

### Feature Additions
- Multi-vehicle comparison (3+ cars)
- Save and share comparisons
- User accounts with saved preferences
- Export comparisons to PDF
- Advanced filtering options

### Technical Improvements
- Implement caching for faster performance
- Add unit and integration tests
- Deploy to cloud platform (Heroku/AWS)
- Implement CI/CD pipeline

---

## Attribution & Acknowledgments

### Data Source
- **[2023 Car Model Dataset - All Data You Need](https://www.kaggle.com/datasets/peshimaammuzammil/2023-car-model-dataset-all-data-you-need)** - Comprehensive vehicle specifications database from Kaggle
  - Dataset by: Peshimaam Muzammil
  - Contains 400+ vehicle models with detailed specifications

### External Resources
- **Flask** - Web framework
- **pandas** - Data manipulation and analysis
- **Select2** - Enhanced select boxes
- **jQuery** - DOM manipulation
- **OpenAI GPT-4** - AI chatbot functionality

### AI Usage Disclosure
This project utilized AI assistance for:
- Debugging
- CSS styling optimization
- README structure formatting
- HTML formatting assistance and user interface improvement
- Performance-to-Price equation implementation assistance
- Dataset management assistance
- Vehicle comparison implementation
- Implementation of JQuery for seamless interaction
- General code organization
- Chatbot integration

## Learning Outcomes Achieved

1. Designed and implemented a complete web application from concept to deployment
2. Developed skills in data processing and API integration with Python
3. Learned effective data visualization techniques for complex specifications
4. Improved understanding of user experience design for data-heavy applications
5. Gained proficiency with Flask for creating web applications
6. Implemented best practices for error handling and user feedback

---

## Project Impact

This project successfully addresses the identified problem of making vehicle comparison accessible and understandable. Users can now:
- Make informed decisions based on comprehensive data
- Understand complex specifications through visual aids
- Receive personalized advice through AI assistance
- Compare vehicles efficiently without visiting multiple websites