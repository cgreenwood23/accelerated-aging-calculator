# Accelerated Shelf-life Calculator:
The Accelerated Aging process is based on the relationship of temperature and reaction rate.
This calculator can be used to determine the conditions for an accelerated ageing protocol. The protocol is based on target shelf life of the product and the intended real-time storage conditions.
This calculator can also be used to determine the target shelf life achieved based on the number of real-time days of staging completed at the accelerated aging temperature.

## Calculator Inputs:
| Input | Description | Application Used | Example |
| --- | --- | --- | ---|
| Target Shelf Life | Time in which, under defined conditions, a product retains the desired attibutes of product quality. | Accelerated | 395 Days |
| Accelerated Aging Temperature (TAA) | The temperature which is used to artifically speed up the aging process. | Accelerated/Target | 12C |
| Real-time Ambient Shelf Temperature (TRT) | The temperature at which the product will be kept during its shelf-life. | Accelerated | 4C |
| Q10 Value | The ratio of the velocity of a chemical reaction at a given temperature to that of the same reaction at a temperature 10 °C lower. | Accelerated/Target | 2.0 |
| Number of Real-time days completed | Number of days the product has been kept under accelerated conditions. | Target | 28 Days |

Accelerated Output Example: Stage Product for 228 Days.

Target Output Examples: 49 Days of target Shelf Life Achieved.

## Run Locally:
### Install dependencies:
Using pip:
```sh
pip install 
```

## Usage:
Using pip:
```sh
python3 accelerated_aging_calculator_Final.py
```

## License
MIT License
