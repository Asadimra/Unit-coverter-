import streamlit as st  

def length_conversion(value, from_unit, to_unit):
    # Base unit: meters
    conversion_factors = {
        'Metre': 1,
        'Kilometre': 1000,
        'Centimetre': 0.01,
        'Millimetre': 0.001,
        'Micrometre': 1e-6,
        'Nanometre': 1e-9,
        'Mile': 1609.34,
        'Yard': 0.9144,
        'Foot': 0.3048,
        'Inch': 0.0254,
        'Nautical mile': 1852
    }
    # Convert to base unit first, then to target unit
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def weight_conversion(value, from_unit, to_unit):
    # Base unit: kilograms
    conversion_factors = {
        'Kilograms': 1,
        'Grams': 0.001,
        'Pounds': 0.453592,
        'Ounces': 0.0283495
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def data_transfer_rate_conversion(value, from_unit, to_unit):
    # Base unit: bits per second (bps)
    conversion_factors = {
        'bps': 1,
        'Kbps': 1e3,
        'Mbps': 1e6,
        'Gbps': 1e9,
        'KB/s': 8e3,
        'MB/s': 8e6,
        'GB/s': 8e9
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def digital_storage_conversion(value, from_unit, to_unit):
    # Base unit: bytes
    conversion_factors = {
        'Bytes': 1,
        'KB': 1024,
        'MB': 1024**2,
        'GB': 1024**3,
        'TB': 1024**4
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def energy_conversion(value, from_unit, to_unit):
    # Base unit: joules
    conversion_factors = {
        'Joules': 1,
        'Kilojoules': 1000,
        'Calories': 4.184,
        'Kilocalories': 4184,
        'Watt-hours': 3600,
        'Kilowatt-hours': 3.6e6
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def frequency_conversion(value, from_unit, to_unit):
    # Base unit: hertz
    conversion_factors = {
        'Hz': 1,
        'kHz': 1e3,
        'MHz': 1e6,
        'GHz': 1e9
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def fuel_economy_conversion(value, from_unit, to_unit):
    # First convert to L/100km as base
    if from_unit == 'MPG (US)':
        base = 235.215 / value
    elif from_unit == 'MPG (UK)':
        base = 282.481 / value
    else:  # L/100km
        base = value
    
    if to_unit == 'MPG (US)':
        return 235.215 / base
    elif to_unit == 'MPG (UK)':
        return 282.481 / base
    return base

def plane_angle_conversion(value, from_unit, to_unit):
    # Base unit: radians
    conversion_factors = {
        'Radians': 1,
        'Degrees': 0.0174533,
        'Gradians': 0.015708,
        'Minutes': 0.000290888,
        'Seconds': 4.84814e-6
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def pressure_conversion(value, from_unit, to_unit):
    # Base unit: Pascal
    conversion_factors = {
        'Pascal': 1,
        'kPa': 1000,
        'Bar': 100000,
        'PSI': 6894.76,
        'mmHg': 133.322,
        'Atmosphere': 101325
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def speed_conversion(value, from_unit, to_unit):
    # Base unit: meters per second
    conversion_factors = {
        'm/s': 1,
        'km/h': 0.277778,
        'mph': 0.44704,
        'knots': 0.514444,
        'ft/s': 0.3048
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def volume_conversion(value, from_unit, to_unit):
    # Base unit: cubic meters
    conversion_factors = {
        'Cubic Meters': 1,
        'Liters': 0.001,
        'Milliliters': 1e-6,
        'Cubic Feet': 0.0283168,
        'Cubic Inches': 1.63871e-5,
        'Gallons (US)': 0.00378541,
        'Quarts (US)': 0.000946353
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def time_conversion(value, from_unit, to_unit):
    # Base unit: seconds
    conversion_factors = {
        'Seconds': 1,
        'Minutes': 60,
        'Hours': 3600,
        'Days': 86400,
        'Weeks': 604800,
        'Months': 2.628e+6,
        'Years': 3.156e+7
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def main():
    st.set_page_config(page_title="Advanced Unit Converter", layout="wide")
    
    # Initialize conversion history in session state if it doesn't exist
    if 'conversion_history' not in st.session_state:
        st.session_state.conversion_history = []
    
    # Add custom CSS
    st.markdown("""
        <style>
        .stSelectbox {
            margin-bottom: 10px;
        }
        .main {
            padding: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title('Advanced Unit Converter')
    
    # Dictionary mapping conversion types to their units and conversion functions
    conversion_options = {
      
        'Data Transfer Rate': {
            'units': ['bps', 'Kbps', 'Mbps', 'Gbps', 'KB/s', 'MB/s', 'GB/s'],
            'function': data_transfer_rate_conversion
        },
        'Digital Storage': {
            'units': ['Bytes', 'KB', 'MB', 'GB', 'TB'],
            'function': digital_storage_conversion
        },
        'Energy': {
            'units': ['Joules', 'Kilojoules', 'Calories', 'Kilocalories', 'Watt-hours', 'Kilowatt-hours'],
            'function': energy_conversion
        },
        'Frequency': {
            'units': ['Hz', 'kHz', 'MHz', 'GHz'],
            'function': frequency_conversion
        },
        'Fuel Economy': {
            'units': ['MPG (US)', 'MPG (UK)', 'L/100km'],
            'function': fuel_economy_conversion
        },
        'Length': {
            'units': ['Metre', 'Kilometre', 'Centimetre', 'Millimetre', 'Micrometre', 
                     'Nanometre', 'Mile', 'Yard', 'Foot', 'Inch', 'Nautical mile'],
            'function': length_conversion
        },
        'Mass': {
            'units': ['Kilograms', 'Grams', 'Pounds', 'Ounces'],
            'function': weight_conversion
        },
        'Plane Angle': {
            'units': ['Radians', 'Degrees', 'Gradians', 'Minutes', 'Seconds'],
            'function': plane_angle_conversion
        },
        'Pressure': {
            'units': ['Pascal', 'kPa', 'Bar', 'PSI', 'mmHg', 'Atmosphere'],
            'function': pressure_conversion
        },
        'Speed': {
            'units': ['m/s', 'km/h', 'mph', 'knots', 'ft/s'],
            'function': speed_conversion
        },
        'Temperature': {
            'units': ['Celsius', 'Fahrenheit', 'Kelvin'],
            'function': temperature_conversion
        },
        'Time': {
            'units': ['Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Months', 'Years'],
            'function': time_conversion
        },
        'Volume': {
            'units': ['Cubic Meters', 'Liters', 'Milliliters', 'Cubic Feet', 'Cubic Inches', 'Gallons (US)', 'Quarts (US)'],
            'function': volume_conversion
        }
    }
    
    # Create columns for better layout
    col1, col2= st.columns([1, 2])
    
    with col1:
        # Conversion type selection
        conversion_type = st.selectbox(
            'Select Conversion Type',
            list(conversion_options.keys())
        )
        
        # Input value
        value = st.number_input('Enter value:', value=0.0)
    
    with col2:
        # Create two columns for from/to units
        subcol1, subcol2 = st.columns(2)
        
        units = conversion_options[conversion_type]['units']
        convert_func = conversion_options[conversion_type]['function']
        
        with subcol1:
            from_unit = st.selectbox('From:', units)
        
        with subcol2:
            to_unit = st.selectbox('To:', units)
    
    # Perform conversion
    if st.button('Convert', key='convert_button'):
        try:
            result = convert_func(value, from_unit, to_unit)
            result_text = f'{value:,.4f} {from_unit} = {result:,.4f} {to_unit}'
            st.success(result_text)
            
            # Add to history with timestamp
            from datetime import datetime
            history_entry = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'type': conversion_type,
                'conversion': result_text
            }
            st.session_state.conversion_history.insert(0, history_entry)  # Add to start of list
        except Exception as e:
            st.error(f'Error during conversion: {str(e)}')
    
    # Display conversion history
    st.markdown("---")
    st.subheader("Conversion History")
    
    if not st.session_state.conversion_history:
        st.info("No conversion history yet")
    else:
        # Add a clear history button
        if st.button("Clear History"):
            st.session_state.conversion_history = []
            st.rerun()
        
        # Display history in a nice format
        for entry in st.session_state.conversion_history:
            with st.container():
                st.text(f"[{entry['timestamp']}] {entry['type']}")
                st.text(f"➜ {entry['conversion']}")
                st.markdown("---")

    # Add helpful information
    with st.expander("Help & Information"):
        st.markdown("""
        ### How to use this converter:
        1. Select the type of conversion you want to perform
        2. Enter the value you want to convert
        3. Select the unit you're converting from
        4. Select the unit you want to convert to
        5. Click the 'Convert' button to see the result
        
        ### Notes:
        - The converter handles a wide range of units and conversion types
        - Results are rounded to 4 decimal places
        - For temperature conversions, the formulas take into account the different scales
        """)

if __name__ == '__main__':
    main()
