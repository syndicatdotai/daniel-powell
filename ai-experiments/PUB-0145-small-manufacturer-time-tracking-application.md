# Building a Time-Tracking Application for a Small Manufacturer

A small Connecticut manufacturer with approximately four employees approached me with a straightforward need: keep track of employee hours without paying for a larger software suite.

The business needed a shared interface where workers could clock in and out, along with a separate owner view showing who was currently clocked in and the hours recorded. The scope was deliberately narrow. A simple application tailored to the company’s existing routine could provide the functionality it needed.

Using AI and ChatGPT Sites, I built, tested, and delivered the application to production in approximately two hours.

## Designing Around the Workplace

The main application was designed to run on a tablet in the office. Employees would use that shared device to identify themselves and clock in or out.

That arrangement fit the scale of the business. It provided a consistent place to record time without requiring every worker to install an application or manage another tool on a personal phone.

The tablet interface was restricted to the information and actions workers needed. Keeping that view focused made the application easier to understand and reduced the opportunity to change information outside the employee workflow.

The owner had a different set of requirements: visibility into who was working and how many hours had been recorded. A separate owner panel provided that view without adding administrative information to the shared employee screen.

## Separating Employee Actions From Owner Oversight

Although the application was small, the distinction between employee and owner access was an important design decision.

The employee interface supported the immediate task of recording attendance. The owner view supported oversight of those records. Defining those responsibilities gave the AI a clear basis for creating the application’s screens and access privileges.

This was a practical exercise in translating a business request into software requirements. “Keep track of time” sounds simple, but it still requires decisions about who enters information, where they enter it, what they can see, and how the person running the business reviews the result.

Resolving those questions early helped keep the application focused throughout development.

## Using AI to Build and Test the Application

I tasked AI with creating the application in ChatGPT Sites, directing the work around the manufacturer’s requirements.

My role was to define the operating workflow, establish the distinction between employee and owner access, review the generated application, and test whether it supported the intended use.

The development process centered on the actual interaction: a worker approaching the office tablet to clock in or out, followed by the owner reviewing attendance and recorded hours through a separate panel.

Working through that complete sequence kept the review tied to the business problem. The application needed to make sense to the people using it in the workplace, as well as function technically.

The full process—from defining the requirements through building, testing, and production delivery—took approximately two hours.

## A Small Application With a Defined Business Purpose

This experiment illustrates the value of building software at the scale of the problem.

For a manufacturer with approximately four employees, a focused time tracker could address a specific administrative need with a limited interface and a short development cycle. The business requirements supplied the boundaries: a shared office tablet, straightforward employee actions, and an owner view for reviewing time.

The result was a production application built around an existing workplace routine. It also provided a concrete example of how AI-assisted development can make a narrowly scoped business tool practical to create and deliver.
