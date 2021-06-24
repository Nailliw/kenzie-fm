from rest_framework.permissions import BasePermission


class ShowPermission(BasePermission):
    message = "não adianta davis ..."

    def has_permission(self, request, view):
        # se for uma operação de leitura returna True antecipadamente
        if request.method == "GET":
            return True

        # se for operação de create, update ou delete
        # ai precisa verificar de o usuario pertence a band

        band = request.user.band

        if band and request.user.band.id == view.kwargs["band_id"]:
            return True
