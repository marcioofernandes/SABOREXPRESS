def int_to_roman(number: int) -> str:
    if not (1 <= number < 4000):
        raise ValueError("The number must be between 1 and 3999.")
    
    # Mapeamento dos números inteiros para os números romanos
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ""
    
    # Loop para encontrar os valores correspondentes
    for value, roman in roman_map:
        while number >= value:  # Enquanto o número atual for maior ou igual ao valor
            result += roman     # Adiciona o símbolo romano ao resultado
            number -= value     # Subtrai o valor correspondente do número
    
    return result

print (int_to_roman(1989))

def roman_to_int(roman: str) -> int:
    # Mapeamento dos símbolos romanos para seus valores inteiros
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Percorre cada símbolo romano na string
    for char in roman:
        current_value = roman_values[char]
        
        # Se o valor atual for maior que o anterior, subtrai o anterior duas vezes (para corrigir soma anterior)
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        
        # Atualiza o valor anterior para a próxima iteração
        prev_value = current_value
    
    return total

print (roman_to_int("IX"))  