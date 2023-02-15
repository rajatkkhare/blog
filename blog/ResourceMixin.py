from blog.app import db


class ResourceMixin(object):
    def save(self):
        """
        Save a model instance.

        :return: Model instance
        """
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def b_update(cls, q_obj, values):
        """
        Bulk Update a model.
        :param q_obj:
        :param values:
        :return: class
        """
        q_obj.update(values, synchronize_session="fetch")
        db.session.commit()
        return cls

    def delete(self):
        """
        Delete a model instance.

        :return: db.session.commit()'s result
        """
        db.session.delete(self)
        return db.session.commit()

    def __str__(self):
        """
        Create a human-readable version of a class instance.

        :return: self
        """
        obj_id = hex(id(self))
        columns = self.__table__.c.keys()

        values = ", ".join("%s=%r" % (n, getattr(self, n)) for n in columns)
        return "<%s %s(%s)>" % (obj_id, self.__class__.__name__, values)
