# An interactive demonstration of social distancing based on a statistical dynamic model of infectious disease

_Chris von Csefalvay_

By far one of the most widespread ways to understand infectious disease in a population is the Kermack-McKendrick compartmental model. Given a population of size $n$, the Kermack-McKendrick model determines the distribution of three subsets of this population: susceptible ($S$), infectious/infected ($I$) and removed ($R$), which includes deceased and immune. Under the assumption that surviving a particular illness provides immunity at least for as long as we are calculating values, the dynamics of the epidemic can be described by a system of differential equations

$$ \frac{dS}{dt} = - \frac{\beta S I}{n} $$

$$ \frac{dI}{dt} = \frac{\beta S I}{n} - \gamma I $$

$$ \frac{dR}{dt} = \gamma I $$

Because we assume static demographics, $S + I + R = n$ and $\frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt} = 0$.

Now let us assume that the variable $\delta(t)$ describes that population's adherence to social distancing, where $1$ denotes perfect social distancing and $0$ denotes no social distancing at all. Because social distancing affects encounter rate, $\beta$, we can reformulate the above differential equations as


$$ \frac{dS}{dt} = - \frac{\beta S I - \beta \delta S I}{n} $$

$$ \frac{dI}{dt} = \frac{\beta S I - \beta \delta S I}{n} - \gamma I $$

$$ \frac{dR}{dt} = \gamma I $$

We can furthermore infer $\beta$ from the relationship

$$ R0 = \frac{\beta}{\gamma} $$

and we can infer $\gamma$, being the inverse of $\tau$, the average duration of illness. This allows us to model the compartment sizes over time as a function of $R_0$, $\tau$ and $\delta$. The model below is based on a total initial population of 10,000, with an initial seed population of 0.1% infected initially.