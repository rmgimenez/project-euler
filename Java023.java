package testejava;

public class Java023
{
    public static void main(String[] args)
    {
        int resultado = 0;
        for (int i = 1; i < 10000; i++)
        {
            int somaDivNum = somaDivisores(i);
            int somaDivNovoNum = 0;
            somaDivNovoNum = somaDivisores(somaDivNum);

            if (i == somaDivNovoNum && i != somaDivNum)
            {
                //System.out.println(i);
                resultado = resultado + i;
            }
        }
        System.out.println(resultado);
    }

    public static int somaDivisores(int num)
    {
        int soma = 0;
        int contador = num / 2;
        while (contador != 0)
        {
            if (num % contador == 0)
            {
                soma += contador;
            }
            contador -= 1;
        }
        return soma;
    }
}
