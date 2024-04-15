from casa_builder import ModernaBuilder, Edificio

class Construccion:
    def make_casa(self, builder):
        builder.set_columns()
        builder.set_interior()
        builder.set_fachada()
        return builder.casa