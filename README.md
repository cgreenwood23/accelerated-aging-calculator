# Accelerated Aging Calculator:
The Accelerated Aging process is based on the relationship of temperature and reaction rate.
This calculator can be used to determine the conditions for an accelerated ageing protocol. The protocol is based on target shelf life of the product and the intended real-time storage conditions.
This calculator can also be used to determine the target shelf life achieved based on the number of real-time days of staging completed at the accelerated aging temperature.

## Calculator Inputs:
| Input | Description | Application Used | Example |
| --- | --- | --- | ---|
| Target Shelf Life | - | Accelerated | 395 Days |
| Accelerated Aging Temperature (TAA) | - | Accelerated/Target | 12C |
| Real-time Ambient Shelf Temperature (TRT) | - | Accelerated | 4C |
| Q10 Value | - | Accelerated/Target | 2.0 |
| Number of Real-time days completed | - | Target | 28 Days |

Accelerated Output Example: Stage Product for 228 Days.

Target Output Examples: 49 Days of target Shelf Life Achieved.

## How to run:
```sh
python3 accelerated_aging_calculator.py
```

## License
MIT License