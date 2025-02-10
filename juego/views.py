import random
from django.shortcuts import render
from django.http import JsonResponse

def iniciar_juego(request):
    return render(request, 'juego/iniciar.html')

def generar_numero_secreto():
    """Genera un número aleatorio de 4 dígitos sin repetir."""
    return "".join(map(str, random.sample(range(10), 4)))

def jugar(request):
    """Maneja el juego y usa sesiones para almacenar el estado."""
    if "numero_secreto" not in request.session:
        request.session["numero_secreto"] = generar_numero_secreto()
        request.session["intentos"] = 7
        request.session["historial"] = []

    numero_secreto = request.session["numero_secreto"]
    intentos = request.session["intentos"]
    historial = request.session["historial"]

    if request.method == "POST":
        intento = request.POST.get("numero")

        if not intento.isdigit() or len(intento) != 4 or len(set(intento)) != 4:
            return JsonResponse({"error": "Número inválido, debe ser de 4 dígitos sin repetir."})

        puntos = sum(1 for i in range(4) if numero_secreto[i] == intento[i])
        famas = sum(1 for i in range(4) if intento[i] in numero_secreto and intento[i] != numero_secreto[i])

        historial.append({"numero": intento, "puntos": puntos, "famas": famas})
        request.session["historial"] = historial
        request.session["intentos"] -= 1
        intentos -= 1

        if puntos == 4:
            request.session.flush()  # Reiniciar sesión
            return JsonResponse({"mensaje": "¡Ganaste!", "historial": historial})

        if intentos == 0:
            numero_correcto = numero_secreto
            request.session.flush()
            return JsonResponse({"mensaje": f"Perdiste. El número era {numero_correcto}", "historial": historial})

        return JsonResponse({"mensaje": f"{puntos} Puntos, {famas} Famas", "historial": historial})

    return render(request, "juego.html", {"historial": historial})
