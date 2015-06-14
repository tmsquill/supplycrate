__author__ = 'Zivia'

import marketmanipulator.items as it
import marketmanipulator.datadb as db
import marketmanipulator.dataservice as ds
import marketmanipulator.datautils as du


def update_items(items_ids=[]):

    if len(items_ids) > 0:

        pass

    else:

        db.drop_table('scratch_items')
        db.create_table('scratch_items')
        db.drop_table('json_items')
        db.create_json_table('json_items')

        items_ids = du.chunks(it.items(), 200)

        for items_ids_group in items_ids:

            items = it.items(items_ids_group)

            print ds.pretty_json(items)

            db.insert(items=items, scratch=True)

        db.compare(items=True)

if __name__ == "__main__":

    update_items()
