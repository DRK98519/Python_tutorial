## Packages
# Package is a folder containing modules and probably sub-packages

import ecommerce.shipping        # import the entire module shipping from the package ecommerce
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping    # import the particular function calc_shipping from the module shipping
                                                # from the package ecommerce
calc_shipping()


from ecommerce.shipping import calc_tax, eval_reliability   # import multiple particular functions (calc_tax,
                                                            # eval_reliability) from the module shipping from the
                                                            # package ecommerce
calc_tax()
eval_reliability()

from ecommerce import shipping  # import the particular module shipping from the package ecommerce

shipping.eval_reliability()
shipping.calc_shipping()
shipping.calc_tax()