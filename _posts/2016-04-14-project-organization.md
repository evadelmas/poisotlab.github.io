---
layout: post
title: Project organization and reproducible code
author: tim
tags: reproducibility
---

An easy step towards making your research reproducible is containment:
everything is a box, with one clear way in, and one clear way out. This is
why programming with functions is great. The arguments are the way in, and
the output is the way out. For example, in the following function, there is
a way in through the `stuff` argument, and one way out as a boolean value
indicating whether or not [it will blend][blend].

[blend]: https://www.youtube.com/watch?v=lBUJcD6Ws6s

~~~ r
will_it_blend <- function(stuff="iphone") {
    return stuff %in% c("iphone", "ice", "rake")
}
~~~

This function does not need to know about anything external, nor does it
needs to know about its surrounding. One you have put in the argument, it will
give you the same output regardless of the state of *e.g.* other variables.

Of course a better way to write this function would be *not* to hard-code
the names of things that will blend in the body of the function itself,
and instead to be able to use a list as another argument. Which we can do as:

~~~ r
will_it_blend <- function(stuff="iphone", stuff_that_usually_blends){
    return stuff %in% stuff_that_usually_blends
}
~~~

Now, calling this function *will* depends on what you give as
`stuff_that_usually_blends`. But again, what happens within the function
is entirely independent from what happens outside of it. This is usually
regarded as a *Good Thing* (the caps means it's not simply a *good thing*,
which is *good*, but not, y'know, *Good*).

So anyways, projects.

I tend to (and therefore [fellow lab members][people] usually humor me)
design projects in a similar way. Nothing exists outside of *the project*. By
the project, I mean a folder located somewhere on my computer in which there
are files related to a future paper.

[people]: /people/

It usually go something like this:

~~~
/project
    /data
    /manuscripts
    /code
    /figures
    Makefile
    LICENSE
    README
    CONTRIBUTING
~~~

The code reads data from their folder, produces figures that go in
their folder, and the manuscript calls everything it needs. This is all
automated thanks to the magic of [makefiles], which these days tend to be
self-[documented].

[makefiles]: http://swcarpentry.github.io/make-novice/
[documented]: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

A very important point is that a piece of code called,
for example `code/make_figure_1.r` will go look for data in
`data/observations.csv`, and write in `figure/figure_1.pdf`. This
is *very* different from having the *absolute path* (for example
`/home/tpoisot/projects/explorations/qc_rangemaps/`) in front every time.

We often work on several machines (our laptops/desktops in the
lab, our trustworthy `ada` for medium-scale jobs, and Compute
Québec machines when we need a lot of results). As a result,
a project that lives at `/home/tpoisot/projects/wherever/` on
my laptop can live at `/home/tpoisot/wherever/` on `ada`, and at
`/home/some_long_unique_id/scratch/running/wherever/` on Compute
Québec. Relying on *absolute paths* means that I would have to maintain three
different versions of the code *just to deal with this*. Using *relative
paths* instead means that as long as I navigate to where the project is,
it will all work on any machine.

And as I am wont to do, I recently explained this point in a calm, cogent,
and didactic way on twitter:

<blockquote class="twitter-tweet" data-lang="fr"><p lang="en" dir="ltr">If the first line of your <a href="https://twitter.com/hashtag/rstats?src=hash">#rstats</a> script is &quot;setwd(...&quot; I will come into your lab and SET YOUR COMPUTER ON FIRE.</p>&mdash; Timothée Poisot (@tpoi) <a href="https://twitter.com/tpoi/status/720340395901648897">13 avril 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Y'all should follow me, I'm charming.
