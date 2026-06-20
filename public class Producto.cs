public class Producto
{
public string Nombre { get; set; }
public double Precio { get; set; }

public void MostrarInformacion()
{
    Console.WriteLine($"Producto: {Nombre} - Precio: {Precio}");
}

}