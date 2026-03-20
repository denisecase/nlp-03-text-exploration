# Glossary (Module 3: Text Exploration)

## Corpus

A collection of text documents used for analysis.
In this project, each document is a short sentence with an associated category.

## Document

A single unit of text within a corpus.
In this project, each document is represented as one line of text.

## Category

A label assigned to a document that groups it with similar documents
(e.g., "dog", "cat", "car", "truck").

## Token

A word-like unit extracted from text during tokenization.

## Tokenization

The process of splitting text into individual tokens (words).

## Cleaning (Text Cleaning)

The process of preparing text for analysis by:

- converting to lowercase
- removing punctuation
- filtering out very short tokens

## Token DataFrame

A tabular structure where each row represents a single token and its associated category.

## Frequency Distribution

A count of how often each token appears.

## Global Frequency

Token frequency calculated across the entire corpus.

## Category Frequency

Token frequency calculated within each category.

## Co-occurrence

A measure of which tokens appear near each other in text.

## Context Window

The number of tokens before and after a target token used to define its context.

## Co-occurrence Dictionary

A dictionary where:

- each key is a token
- each value is a list of tokens that appear near it

## Bigram

A pair of consecutive tokens (two-word sequence).

## Bigram Frequency

A count of how often each bigram appears.

## Visualization

A graphical representation of data (e.g., bar charts of token frequencies).

## Pattern

A repeated structure in the data, such as:

- words appearing in similar contexts
- tokens clustering by category

## Interpretation

The process of explaining what the results mean based on observed patterns in the data.
